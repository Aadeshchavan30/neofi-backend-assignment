
from app.models.version import EventVersion
from app.models.event import Event

async def save_event_version(event):
    event_data = {
        "title": event.title,
        "description": event.description,
        "start_time": str(event.start_time),
        "end_time": str(event.end_time),
        "location": event.location,
        "is_recurring": event.is_recurring,
        "recurrence_pattern": event.recurrence_pattern
    }
    await EventVersion.create(event=event, data=event_data)

async def get_event_version(event_id: int, version_id: int):
    version = await EventVersion.get(id=version_id, event_id=event_id)
    return version.data

async def rollback_event(event_id: int, version_id: int):
    version = await EventVersion.get(id=version_id, event_id=event_id)
    event = await Event.get(id=event_id)
    for key, value in version.data.items():
        setattr(event, key, value)
    await event.save()
    return {"message": "Rolled back", "version_id": version_id}
