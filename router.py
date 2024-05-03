from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import crud

from Auth import database
from Auth.database import get_async_session
from models.models import event
from Auth.schemas import EventCreate,Event

from typing import List

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


#--------------------------------------------------------------------------------------------------------
@router.get("/")
# def get_events():
#     return
async def get_events(event_name: str, session: AsyncSession = Depends(get_async_session)):
    query = select(event).where(event.c.name == event_name)
    #query = f"SELECT * FROM event WHERE name = {event_name}"
    result = await session.execute(query)
    #return result.all()
    return {*result.all()}
@router.post("/")
async def add_event(new_event: EventCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(event).values(**new_event.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}