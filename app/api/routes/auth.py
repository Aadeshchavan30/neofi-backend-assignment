
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, Token
from app.services.auth import register_user, login_user

router = APIRouter()

@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    return await register_user(user)

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_user(form_data.username, form_data.password)
