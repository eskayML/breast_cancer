from app import app, COLUMNS
import pytest
OPENAI_KEY = "0sgcsjsygscjxxkeu26svvsnsu1kvsvvavmm"
def test_index():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200


def test_predict():
    with app.test_client() as client:
        response = client.get("/predict")
        assert response.status_code == 200


def test_submit_form():
    dummy_values = [1] * 10
    with app.test_client() as client:
        response = client.post("/predict", data=dict(zip(COLUMNS, dummy_values)))
        assert b"The model predicted" in response.data
