from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

class Poll(BaseModel):
    question: str
    option_a: str
    option_b: str

class Vote(BaseModel):
    poll_id: int
    option: str  # "A" or "B"
