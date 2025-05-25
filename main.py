from fastapi import FastAPI
from app.database import init_db
from app.api.routes import auth, events, share, version

app = FastAPI()

app.include_router(auth.router, prefix='/api/auth')
app.include_router(events.router, prefix='/api/events')
app.include_router(share.router, prefix='/api/events')
app.include_router(version.router, prefix='/api/events')

@app.on_event('startup')
async def startup():
    await init_db()