
from tortoise import fields, models

class Event(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    description = fields.TextField()
    start_time = fields.DatetimeField()
    end_time = fields.DatetimeField()
    location = fields.CharField(max_length=255, null=True)
    is_recurring = fields.BooleanField(default=False)
    recurrence_pattern = fields.CharField(max_length=255, null=True)
    owner = fields.ForeignKeyField("models.User", related_name="events")
