
from app.models.event import Event
from app.schemas.event import EventCreate, EventOut
from app.services.versioning import save_event_version

async def create_event(event: EventCreate):
    user_id = 1  # mock current user
    new_event = await Event.create(
        title=event.title,
        description=event.description,
        start_time=event.start_time,
        end_time=event.end_time,
        location=event.location,
        is_recurring=event.is_recurring,
        recurrence_pattern=event.recurrence_pattern,
        owner_id=user_id
    )
    await save_event_version(new_event)
    return await EventOut.from_tortoise_orm(new_event)
