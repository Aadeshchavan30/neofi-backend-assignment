
from tortoise import fields, models

class Permission(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="permissions")
    event = fields.ForeignKeyField("models.Event", related_name="permissions")
    role = fields.CharField(max_length=10)  # Owner, Editor, Viewer
