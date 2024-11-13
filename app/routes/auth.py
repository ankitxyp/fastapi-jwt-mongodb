from fastapi import APIRouter, HTTPException
from app.services.user_service import authenticate_user, create_user
from app.models.user import UserCreate

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    await create_user(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(email: str, password: str):
    token = await authenticate_user(email, password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
