from pydantic import BaseModel


class SomeInput(BaseModel):
    num: int


class SomeOutput(BaseModel):
    result: int
