
from fastapi import APIRouter
from app.schemas.share import ShareRequest, PermissionOut
from app.services.share import share_event, list_permissions

router = APIRouter()

@router.post("/{event_id}/share", response_model=list[PermissionOut])
async def share(event_id: int, data: ShareRequest):
    return await share_event(event_id, data)

@router.get("/{event_id}/permissions", response_model=list[PermissionOut])
async def permissions(event_id: int):
    return await list_permissions(event_id)
