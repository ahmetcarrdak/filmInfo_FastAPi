from film_info_project.app.models.actor import Actor
from sqlalchemy.orm import Session

class ActorService:
    def __init__(self, db: Session):
        self.db = db

    def get_actor(self, actor_id: int):
        return self.db.query(Actor).filter(Actor.id == actor_id).first()

    def create_actor(self, actor_data):
        db_actor = Actor(**actor_data)
        self.db.add(db_actor)
        self.db.commit()
        self.db.refresh(db_actor)
        return db_actor

    def get_all_actors(self):
        return self.db.query(Actor).all()
