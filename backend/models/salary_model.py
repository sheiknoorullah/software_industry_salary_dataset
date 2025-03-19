from pydantic import BaseModel


class PredictionInput(BaseModel):
    Rating: float
    Job_Title: str
    Location: str
    Employment_Status: str
