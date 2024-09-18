from fastapi.testclient import TestClient
from film_info_project.app.main import app

client = TestClient(app)

def test_create_actor():
    response = client.post("/actors/", json={"name": "Test Actor", "birth_year": 1980})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Actor"
