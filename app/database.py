from tortoise import Tortoise

async def init_db():
    await Tortoise.init(db_url='sqlite://db.sqlite3', modules={'models': ['app.models.user', 'app.models.event', 'app.models.permissions', 'app.models.version']})
    await Tortoise.generate_schemas()