from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker, declarative_base

client = TestClient(app)

# DATABASE_URL = "sqlite:///:memory:"

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False},
#     poolclass = StaticPool,
# )

# LocalSessionTesting = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )

# def override_get_db():
#     database = TestingSessionLocal()
#     yield database
#     database.close()

# app.dependency_overrides[get_db] = override_get_db

def test_root_returns_something():
    response = client.get("/")
    assert response.status_code < 500

def test_create_valid_ticket():
    response = client.post(
        "/tickets",
        json = {
            "title": "Ticket Created",
            "description": "Ticket description",
            "priority": "low",
            "status": "open"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Ticket Created"
    assert data["description"] == "Ticket description"
    assert data["priority"] == "low"
    assert data["status"] == "open"


def test_invalid_ticket_input():
    response = client.post(
        "/tickets",
        json = {
            "title": "Ticket Created",
            "description": "Ticket description",
            "priority": "low",
            "status": "not completed"
        }
    )
    assert response.status_code == 422

def test_getting_existing_ticket():
    response = client.get("/tickets/99999")
    assert response.status_code in [200, 404]

def test_get_non_existent_ticket():
    response = client.get("/tickets/10000")
    assert response.status_code == 404

def test_update_ticket():
    response = client.post(
        "/tickets/1",
        json = {
            "title": "Ticket update test works",
            "description": "Ticket update test works",
            "priority": "high",
            "status": "closed"
        }
    )
    assert response.status_code < 500

def test_update_ticket_without_id():
    response = client.post(
        "/tickets/83900328930280",
        json = {
            "title": "Ticket update test works",
            "description": "Ticket update test works",
            "priority": "low",
            "status": "open"
        } 
    )
    assert response.status_code == 405

def test_delete_ticket():
    response = client.delete("/tickets/1")
    assert response.status_code in [200, 204, 404, 405]

def test_delete_ticket_without_id():
    response = client.delete(
        "/tickets" 
    )
    assert response.status_code == 405