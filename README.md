# FastAPI JWT MongoDB Project

## Project Description
This project is a user authentication system using JWT with FastAPI and MongoDB.

### Features
- User registration and login
- JWT-based authentication
- Secure endpoints for user CRUD
- MongoDB as the database
- Password hashing

### Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file with the following variables:
   ```
MONGODB_URI="mongodb+srv://ankitdudo9128:Q2LFWcqVHITLrcKT@cluster0.nhcyx.mongodb.net/"
DATABASE_NAME="Cluster0"
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

   ```
3. Run the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

### Scripts
- `scripts/create_user.py`: Script to create a default admin user.

### API Endpoints
- `POST /auth/register`: Register a new user.
- `POST /auth/login`: Login and receive a JWT token.
