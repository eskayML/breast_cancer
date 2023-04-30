from app import app, COLUMNS
import pytest

def test_index():
    with app.test_client() as client:
        response = client.get('/')

        assert response.status_code == 200




def test_predict_page():
    dummy_values = [1]*10
    with app.test_client() as client:
        response = client.post('/predict', data = dict(zip(COLUMNS, dummy_values)))
        assert response.status_code == 200

        assert  b'The model predicted' in response.data
        