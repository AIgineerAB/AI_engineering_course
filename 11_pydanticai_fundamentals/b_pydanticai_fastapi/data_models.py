from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str
    year: int
    genre: str
    rating: int = Field(gt=0, lt=6)


class Prompt(BaseModel):
    prompt: str
