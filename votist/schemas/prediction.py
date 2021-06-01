from pydantic import BaseModel


class PredictionSchema(BaseModel):
    fraudulent: bool
