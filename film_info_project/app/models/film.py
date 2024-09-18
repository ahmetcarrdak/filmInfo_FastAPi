from sqlalchemy import Column, Integer, String
from film_info_project.app.db import Base


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    release_year = Column(Integer)
    genre = Column(String)
