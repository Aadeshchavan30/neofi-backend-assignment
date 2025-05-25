
from fastapi import APIRouter
from app.services.versioning import get_event_version, rollback_event

router = APIRouter()

@router.get("/{event_id}/history/{version_id}")
async def get_version(event_id: int, version_id: int):
    return await get_event_version(event_id, version_id)

@router.post("/{event_id}/rollback/{version_id}")
async def rollback(event_id: int, version_id: int):
    return await rollback_event(event_id, version_id)
