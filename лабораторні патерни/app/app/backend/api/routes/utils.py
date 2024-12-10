# utils.py
from typing import Dict
from urllib.parse import urlencode
from backend.config import TRANSLATE_API_KEY

def build_translation_headers() -> Dict[str, str]:
    """Builds headers for the Google Translate API request.

    Returns:
        Dict[str, str]: Headers required for the API request
    """
    return {
        'x-rapidapi-key': TRANSLATE_API_KEY,
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'Content-Type': "application/x-www-form-urlencoded"
    }

def build_translation_query(text: str, target_language: str, source_language: str = 'auto') -> str:
    """Builds the request body for the Google Translate API.

    Args:
        text (str): Text to translate
        target_language (str): Target language code (e.g., 'en', 'es', 'fr')
        source_language (str): Source language code or 'auto' for auto-detection

    Returns:
        str: URL encoded query string for the translation request
    """
    request_data = {
        'q': text,
        'target': target_language,
        'source': source_language
    }
    return urlencode(request_data)

def build_detection_query(text: str) -> str:
    """Builds the request body for language detection.

    Args:
        text (str): Text to detect language for

    Returns:
        str: URL encoded query string for the detection request
    """
    request_data = {
        'q': text
    }
    return urlencode(request_data)

def get_translation_url(base_url: str, endpoint: str = 'translate') -> str:
    """Builds the full URL for the translation API endpoint.

    Args:
        base_url (str): Base URL of the API
        endpoint (str): Endpoint to use ('translate' or 'detect')

    Returns:
        str: Complete URL for the API request
    """
    endpoints = {
        'translate': '/language/translate/v2',
        'detect': '/language/translate/v2/detect'
    }
    return base_url + endpoints.get(endpoint, endpoints['translate'])