# app/main.py
from fastapi import FastAPI, HTTPException
from app.schemas import UserCreate, QuestionAnswer, UserScore, UserCredits
from app.crud import create_user, get_user_score, update_user_credits
from app.database import metadata, engine

app = FastAPI()

metadata.create_all(bind=engine)


@app.post("/users/", response_model=UserCreate)
async def create_user_endpoint(user: UserCreate):
    await create_user(user)
    return user


@app.get("/users/{user_id}/score", response_model=UserScore)
async def get_user_score_endpoint(user_id: int):
    score = await get_user_score(user_id)
    if score is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserScore(user_id=user_id, score=score[0])


@app.post("/users/{user_id}/credits", response_model=UserCredits)
async def update_user_credits_endpoint(user_id: int, user_credits: UserCredits):
    await update_user_credits(user_credits)
    return user_credits
