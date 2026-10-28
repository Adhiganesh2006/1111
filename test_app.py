from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Kubernetes CI/CD is working" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

# Push 1 Tests: Addition and Subtraction
def test_addition():
    client = app.test_client()
    response = client.post("/calculate", json={"operation": "add", "num1": 10, "num2": 5})
    assert response.status_code == 200
    assert response.json["result"] == 15.0

def test_subtraction():
    client = app.test_client()
    response = client.post("/calculate", json={"operation": "subtract", "num1": 10, "num2": 5})
    assert response.status_code == 200
    assert response.json["result"] == 5.0

# Push 2 Tests: Multiplication and Division
def test_multiplication():
    client = app.test_client()
    response = client.post("/calculate", json={"operation": "multiply", "num1": 4, "num2": 5})
    assert response.status_code == 200
    assert response.json["result"] == 20.0

def test_division():
    client = app.test_client()
    response = client.post("/calculate", json={"operation": "divide", "num1": 10, "num2": 2})
    assert response.status_code == 200
    assert response.json["result"] == 5.0

def test_division_by_zero():
    client = app.test_client()
    response = client.post("/calculate", json={"operation": "divide", "num1": 10, "num2": 0})
    assert response.status_code == 400
    assert "error" in response.json
