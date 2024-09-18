from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from film_info_project.app.schemas.actor import Actor, ActorCreate
from film_info_project.app.services.actor_service import ActorService
from film_info_project.app.main import get_db

router = APIRouter()

@router.post("/", response_model=Actor)
def create_actor(actor: ActorCreate, db: Session = Depends(get_db)):
    service = ActorService(db)
    return service.create_actor(actor.dict())

@router.get("/{actor_id}", response_model=Actor)
def read_actor(actor_id: int, db: Session = Depends(get_db)):
    service = ActorService(db)
    actor = service.get_actor(actor_id)
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@router.get("/", response_model=list[Actor])
def read_actors(db: Session = Depends(get_db)):
    service = ActorService(db)
    return service.get_all_actors()
