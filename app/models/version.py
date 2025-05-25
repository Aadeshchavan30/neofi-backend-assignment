
from tortoise import fields, models

class EventVersion(models.Model):
    id = fields.IntField(pk=True)
    event = fields.ForeignKeyField("models.Event", related_name="versions")
    data = fields.JSONField()
    created_at = fields.DatetimeField(auto_now_add=True)
