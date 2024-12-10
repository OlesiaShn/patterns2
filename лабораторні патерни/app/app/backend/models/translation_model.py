from typing import Optional
from datetime import datetime
from beanie import Document, Indexed
from pydantic import BaseModel, Field

class TranslationSchema(BaseModel):
    source_text: str = Field(..., description="Original text to translate")
    source_language: str = Field(..., description="Source language code")
    target_language: str = Field(..., description="Target language code")
    translated_text: str = Field(..., description="Translated text")
    confidence: float = Field(..., description="Translation confidence score")
    time: datetime = Field(default_factory=datetime.utcnow)
    
class TranslationRecord(Document, TranslationSchema):
    def __repr__(self) -> str:
        return f"<Translation {self.source_language}->{self.target_language}>"

    def __str__(self) -> str:
        return f"{self.source_text} -> {self.translated_text}"

    def __hash__(self) -> int:
        return hash((self.source_text, self.target_language))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TranslationRecord):
            return (self.source_text == other.source_text and 
                   self.target_language == other.target_language)
        return False

    @property
    def created(self) -> datetime:
        return self.id.generation_time

    @classmethod
    async def by_text(cls, source_text: str) -> "TranslationRecord":
        return await cls.find_one({"source_text": source_text})

__beanie_models__ = [TranslationRecord]