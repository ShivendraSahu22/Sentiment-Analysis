from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    predicted_marks: float = Field(
        ...,
        description="The predicted student marks",
        example=85.5
    )