from fastapi.testclient import TestClient
from film_info_project.app.main import app

client = TestClient(app)

def test_create_film():
    response = client.post("/films/", json={"title": "Test Film", "release_year": 2024, "genre": "Drama"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Film"
