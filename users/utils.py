import logging
from jose import jwt
from datetime import datetime, timedelta
from fastapi.security import APIKeyHeader
from fastapi import Security, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from .model import User,get_db



class JWT:
    @staticmethod
    def jwt_encode(data: dict):
        try:
            if 'exp' not in data:
                data.update(exp=datetime.utcnow() + timedelta(hours=2), iat=datetime.utcnow())
            return jwt.encode(data, 'key', algorithm="HS256")
        except jwt.JWTError as err:
            raise err

    @staticmethod
    def jwt_decode(token):
        try:
            return jwt.decode(token, 'key', algorithms=['HS256'])

        except jwt.JWTError as err:
            raise err


api_key = APIKeyHeader(name='Authorization')


def jwt_verification(request: Request, token: str = Security(api_key), db: Session = Depends(get_db)):
    try:
        decode_token = JWT.jwt_decode(token)
        user_id = decode_token.get('user')
        users = db.query(User).filter_by(id=user_id).one_or_none()
        if not users:
            raise HTTPException(status_code=401, detail='User not authorized')
        request.state.user = users
    except Exception as err:
        logging.exception(err.args[0])
