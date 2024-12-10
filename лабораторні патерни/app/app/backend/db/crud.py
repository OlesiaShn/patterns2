from typing import List, Optional
from datetime import datetime
from backend.models.translation_model import TranslationSchema, TranslationRecord

async def create_translation(translation: TranslationSchema) -> TranslationSchema:
    translation_record = TranslationRecord(**translation.model_dump())
    await translation_record.insert()
    return translation

async def get_by_text(source_text: str) -> Optional[TranslationRecord]:
    translation = await TranslationRecord.find_one(
        TranslationRecord.source_text == source_text
    )
    return translation

async def get_all_translations() -> List[TranslationRecord]:
    translations = await TranslationRecord.find_all().to_list()
    return translations

async def update_translation(translation: TranslationSchema) -> TranslationRecord:
    to_update = await TranslationRecord.find_one(
        TranslationRecord.source_text == translation.source_text
    )
    if to_update:
        await to_update.set({
            TranslationRecord.translated_text: translation.translated_text,
            TranslationRecord.confidence: translation.confidence,
            TranslationRecord.time: datetime.utcnow()
        })
    return to_update

async def delete_translation(source_text: str) -> bool:
    to_delete = await TranslationRecord.find_one(
        TranslationRecord.source_text == source_text
    )
    if to_delete:
        await to_delete.delete()
        return True
    return False