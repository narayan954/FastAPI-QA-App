# app/crud.py
from sqlalchemy import select, insert, update
from app.models import users, scores, credits
from app.database import engine
from app.schemas import UserCreate, UserScore, UserCredits


async def create_user(user: UserCreate):
    query = insert(users).values(username=user.username)
    async with engine.begin() as conn:
        await conn.execute(query)


async def get_user_score(user_id: int):
    query = select(scores.c.score).where(scores.c.user_id == user_id)
    async with engine.begin() as conn:
        result = await conn.execute(query)
        return result.fetchone()


async def update_user_credits(user_credits: UserCredits):
    query = (
        update(credits)
        .where(credits.c.user_id == user_credits.user_id)
        .values(credits=user_credits.credits)
    )
    async with engine.begin() as conn:
        await conn.execute(query)
