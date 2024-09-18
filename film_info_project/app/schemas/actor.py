from pydantic import BaseModel

class ActorBase(BaseModel):
    name: str
    birth_year: int

class ActorCreate(ActorBase):
    pass

class Actor(ActorBase):
    id: int

    class Config:
        orm_mode = True
