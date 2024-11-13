import asyncio
from app.services.user_service import create_user

user_data = {
    "email": "admin@example.com",
    "username": "admin",
    "password": "admin123"
}

asyncio.run(create_user(user_data))
