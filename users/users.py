from logger import logger
from fastapi import Response, Request, APIRouter, Depends, status
from .schemas import UserValidator, UserLogin
from .model import User, session, get_db
from sqlalchemy.orm import Session
from passlib.hash import pbkdf2_sha256
from .utils import JWT

router = APIRouter()


@router.post("/registration", status_code=status.HTTP_201_CREATED)
def user_registration(data: UserValidator, db: Session = Depends(get_db)):
    try:
        data = data.dict()
        data['password'] = pbkdf2_sha256.hash(data['password'])
        users = User(**data)
        db.add(users)
        db.commit()
        db.refresh(users)
        return {"message": 'User registered successfully', 'Status': 201, 'data': users}
    except Exception as err:
        logger.exception(err.args[0])
        return {"message": str(err), 'Status': 400, 'data': {}}


@router.post('/login_user/', status_code=status.HTTP_200_OK)
def login_user(user_login: UserLogin, response: Response, db: Session = Depends(get_db)):
    try:
        users = db.query(User).filter_by(username=user_login.username).first()
        if users and pbkdf2_sha256.verify(user_login.password, users.password):
            token = JWT.jwt_encode({'user': users.id})
            return {"message": 'Logged in successfully', 'status': 200, 'access_token': token}
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": 'Invalid username or password', 'status': 401, 'data': {}}
    except Exception as err:
        logger.exception(err.args[0])
        return {'message': err.args[0], 'status': 400, 'data': {}}
