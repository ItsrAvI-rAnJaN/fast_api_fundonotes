from pydantic import BaseModel


class UserValidator(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str
    is_superuser: bool
    location: str
    phone: int
