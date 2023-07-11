from pydantic import BaseModel


class NoteValidator(BaseModel):
    tittle: str
    description: str
    color :str
