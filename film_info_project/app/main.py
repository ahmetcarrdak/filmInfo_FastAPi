from fastapi import FastAPI
from film_info_project.app.api import film_routes, actor_routes
from film_info_project.app.db import engine, Base
from film_info_project.app.config import DATABASE_URL
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI
app = FastAPI()

# Include routers
app.include_router(film_routes.router, prefix="/films", tags=["films"])
app.include_router(actor_routes.router, prefix="/actors", tags=["actors"])

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    try:
        yield db
    finally:
        db.close()
