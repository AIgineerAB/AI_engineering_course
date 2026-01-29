from pydantic import BaseModel, Field

class RagResponse(BaseModel):
    filename: str = Field(description="filename without suffix of retrieved file")
    filepath: str = Field(description="absolute path to retrieved file")
    answer: str = Field(description="answer based on retrieved file")

class Prompt(BaseModel):
    prompt: str 