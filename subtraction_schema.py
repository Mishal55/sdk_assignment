from pydantic import BaseModel

class SubtractionInput(BaseModel):
    minuend: int
    subtrahend: int
