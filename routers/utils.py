from jose import jwt
from datetime import datetime, timedelta



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


