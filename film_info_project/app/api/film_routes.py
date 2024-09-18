from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from film_info_project.app.schemas.film import Film, FilmCreate
from film_info_project.app.services.film_service import FilmService
from film_info_project.app.main import get_db

router = APIRouter()

@router.post("/", response_model=Film)
def create_film(film: FilmCreate, db: Session = Depends(get_db)):
    service = FilmService(db)
    return service.create_film(film.dict())

@router.get("/{film_id}", response_model=Film)
def read_film(film_id: int, db: Session = Depends(get_db)):
    service = FilmService(db)
    film = service.get_film(film_id)
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return film

@router.get("/", response_model=list[Film])
def read_films(db: Session = Depends(get_db)):
    service = FilmService(db)
    return service.get_all_films()
