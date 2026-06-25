from pydantic import BaseModel, Field, field_validator
from typing import Annotated


class SentimentInput(BaseModel):

    text: Annotated[
        str,
        Field(
            ...,
            description="Text for sentiment analysis",
            min_length=1
        )
    ]

    @field_validator("text")
    def validate_text(cls, value):

        if not value.strip():
            raise ValueError(
                "Text cannot be empty"
            )

        return value