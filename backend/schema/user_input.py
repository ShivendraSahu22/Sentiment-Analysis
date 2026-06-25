from pydantic import BaseModel, Field, field_validator
from typing import Annotated

class UserInput(BaseModel):

     number_courses: Annotated[int, Field(..., description="Number of courses taken by the student")]
     time_study: Annotated[float, Field(..., description="Time spent studying")]

     @field_validator('number_courses')
     def validate_number_courses(cls, value):
          if value < 0:
               raise ValueError("Number of courses cannot be negative")
          return value

     @field_validator('time_study')
     def validate_time_study(cls, value):
          if value < 0:
               raise ValueError("Time spent studying cannot be negative")
          return value