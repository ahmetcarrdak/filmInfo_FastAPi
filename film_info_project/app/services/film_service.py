from film_info_project.app.models.film import Film
from sqlalchemy.orm import Session

class FilmService:
    def __init__(self, db: Session):
        self.db = db

    def get_film(self, film_id: int):
        return self.db.query(Film).filter(Film.id == film_id).first()

    def create_film(self, film_data):
        db_film = Film(**film_data)
        self.db.add(db_film)
        self.db.commit()
        self.db.refresh(db_film)
        return db_film

    def get_all_films(self):
        return self.db.query(Film).all()
