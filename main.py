from fastapi import FastAPI,Depends
from users import users
from users.utils import jwt_verification


app = FastAPI()

app.include_router(users.router, prefix="/user")