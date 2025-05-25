
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from jose import jwt
import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"

async def register_user(user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    user_obj = await User.create(username=user.username, email=user.email, hashed_password=hashed_password)
    return create_token(user_obj.id)

async def login_user(username: str, password: str):
    user = await User.get(username=username)
    if not pwd_context.verify(password, user.hashed_password):
        raise Exception("Invalid password")
    return create_token(user.id)

def create_token(user_id: int):
    payload = {
        "sub": str(user_id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
