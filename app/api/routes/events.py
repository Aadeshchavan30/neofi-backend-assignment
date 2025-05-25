
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.event import EventCreate, EventOut
from app.services.events import create_event

router = APIRouter()

@router.post("/", response_model=EventOut)
async def create(event: EventCreate):
    return await create_event(event)
