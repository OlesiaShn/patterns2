from typing import List
import httpx
from fastapi import APIRouter, HTTPException, Body
from backend.api.routes.utils import (
    build_translation_headers,
    build_translation_query,
    get_translation_url,
    build_detection_query
)
from backend.models.translation_model import TranslationSchema
from backend.db.crud import (
    create_translation,
    get_by_text,
    get_all_translations,
    update_translation
)
from backend.config import TRANSLATE_API_KEY

translation_router = APIRouter(include_in_schema=True)
detection_router = APIRouter(include_in_schema=True)
language_router = APIRouter(include_in_schema=True)

BASE_TRANSLATE_URL = "https://google-translate1.p.rapidapi.com"


async def get_translation_data(text: str, target_lang: str, source_lang: str = "auto"):
    """Gets translation data from API"""
    url = f"{BASE_TRANSLATE_URL}/language/translate/v2"

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": TRANSLATE_API_KEY,
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    payload = {
        "q": text,
        "target": target_lang,
        "source": source_lang
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, data=payload)
            response.raise_for_status()  # Raises an exception for 4XX/5XX responses

            data = response.json()
            # Перевіряємо структуру відповіді і дістаємо переклад
            if "data" in data and "translations" in data["data"]:
                translation = data["data"]["translations"][0]
                return {
                    "source_text": text,
                    "translated_text": translation.get("translatedText"),
                    "source_language": translation.get("detectedSourceLanguage", source_lang),
                    "target_language": target_lang
                }
            raise HTTPException(status_code=500, detail="Unexpected API response format")

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Translation API error: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")


@translation_router.post("/translate/", response_model=TranslationSchema)
async def create_translation_record(
        text: str = Body(..., embed=True),
        target_lang: str = Body(..., embed=True),
        source_lang: str = Body("auto", embed=True)
):
    """Creates a new translation record and saves to database"""
    try:
        # Отримуємо дані перекладу
        translation_data = await get_translation_data(
            text=text,
            target_lang=target_lang,
            source_lang=source_lang
        )

        # Створюємо об'єкт TranslationSchema
        translation = TranslationSchema(
            source_text=translation_data["source_text"],
            translated_text=translation_data["translated_text"],
            source_language=translation_data["source_language"],
            target_language=translation_data["target_language"]
        )

        # Зберігаємо в базу даних
        translation_record = await create_translation(translation=translation)
        return translation_record

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@translation_router.get("/translate/{text}", response_model=TranslationSchema)
async def get_translation_by_text(text: str):
    """Gets translation record by source text"""
    translation_record = await get_by_text(source_text=text)
    if translation_record is None:
        raise HTTPException(404, "Translation not found")
    return translation_record


@translation_router.get("/translate/all/", response_model=List[TranslationSchema])
async def get_all_translation_records():
    """Gets all translation records"""
    translations = await get_all_translations()
    if translations is None:
        raise HTTPException(404, "Database is empty")
    return translations


@detection_router.post("/detect")
async def detect_language(text: str):
    """Detects the language of the provided text"""
    url = get_translation_url(BASE_TRANSLATE_URL, 'detect')
    headers = build_translation_headers()
    query = build_detection_query(text)

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=query)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Language detection error")
        return response.json()