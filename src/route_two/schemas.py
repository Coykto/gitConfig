from pydantic import BaseModel


class InputTwo(BaseModel):
    s: str


class OutputTwo(BaseModel):
    result: str
