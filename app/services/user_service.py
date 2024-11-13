from app.database.connection import db
from app.utils.security import hash_password, verify_password
from app.utils.jwt_handler import create_access_token

async def create_user(user_data):
    user_data["hashed_password"] = hash_password(user_data.pop("password"))
    await db["users"].insert_one(user_data)
    return user_data

async def authenticate_user(email, password):
    user = await db["users"].find_one({"email": email})
    if user and verify_password(password, user["hashed_password"]):
        return create_access_token({"sub": user["email"]})
    return None
