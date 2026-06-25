from pydantic import BaseModel, Field


class PredictionResponse(BaseModel):

    predicted_sentiment: str = Field(
        ...,
        description="The predicted sentiment",
        examples=["Positive 😊"]
    )

    predicted_sentiment_score: float = Field(
        ...,
        description="Confidence score",
        examples=[0.95]
    )