
from app.models.permissions import Permission
from app.schemas.share import ShareRequest

async def share_event(event_id: int, data: ShareRequest):
    permissions = []
    for entry in data.users:
        perm, _ = await Permission.get_or_create(user_id=entry.user_id, event_id=event_id)
        perm.role = entry.role
        await perm.save()
        permissions.append({"user_id": entry.user_id, "role": entry.role})
    return permissions

async def list_permissions(event_id: int):
    perms = await Permission.filter(event_id=event_id).all()
    return [{"user_id": p.user_id, "role": p.role} for p in perms]
