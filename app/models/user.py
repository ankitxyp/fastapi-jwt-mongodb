from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserInDB(UserCreate):
    hashed_password: str

class UserResponse(BaseModel):
    email: EmailStr
    username: str
