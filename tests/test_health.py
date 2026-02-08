from fastapi.testclient import TestClient
from ai_digest_agent.main import app

def test_health():
    assert TestClient(app).get("/health").json() == {"status": "ok"}