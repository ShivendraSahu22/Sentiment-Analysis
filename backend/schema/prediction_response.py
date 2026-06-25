from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):

    predicted_seniment: str = Field(
        ...,
        description="The predicted sentiment",
        example="Positive"
    )

    predicted_seniment_score: float = Field(
        ...,
        description="The predicted sentiment score",
        example=85.5
    )