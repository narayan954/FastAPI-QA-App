# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional


class UserCreate(BaseModel):
    username: str


class QuestionAnswer(BaseModel):
    question_id: int
    answer: str
    tags: List[str]


class UserScore(BaseModel):
    user_id: int
    score: int


class UserCredits(BaseModel):
    user_id: int
    credits: int


class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True
