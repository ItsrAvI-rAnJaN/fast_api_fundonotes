from fastapi import Response, Request, APIRouter, Depends, status
from .schemas import UserValidator,UserLogin
from model import User, session, get_db
from sqlalchemy.orm import Session
from passlib.hash import pbkdf2_sha256

router = APIRouter()


@router.post("/registration", status_code=status.HTTP_201_CREATED)
def user_registration(data: UserValidator, db: Session = Depends(get_db)):
    data = data.dict()
    data['password'] = pbkdf2_sha256.hash(data['password'])
    users = User(**data)
    db.add(users)
    db.commit()
    db.refresh(users)
    return {"message": 'User registered successfully', 'Status': 201, 'data': users}


@router.post('/login_user/', status_code=status.HTTP_200_OK)
def login_user(user_login: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=user_login.username).first()
    if user and pbkdf2_sha256.verify(user_login.password, user.password):
        return {"message": 'Logged in successfully', 'status': 200}
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"message": 'Invalid username or password', 'status': 401, 'data': {}}
