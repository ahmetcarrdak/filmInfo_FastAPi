from pydantic import BaseModel

class FilmBase(BaseModel):
    title: str
    release_year: int
    genre: str

class FilmCreate(FilmBase):
    pass

class Film(FilmBase):
    id: int

    class Config:
        orm_mode = True
