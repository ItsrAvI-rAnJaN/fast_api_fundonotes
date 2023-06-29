from fastapi import Response, Request, APIRouter,Depends
from .schemas import UserValidator
from model import User, session,get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/registration")
def user_registration(data: UserValidator, response: Response, request: Request, db: Session = Depends(get_db)):
    data = data.dict()
    users = User(**data)
    db.add(users)
    db.commit()
    db.refresh(users)
    return users
