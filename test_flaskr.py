import pytest
import flaskr


@pytest.fixture
def client():
    app = flaskr.create_app()

    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_index(client):
    """Start with a blank database."""

    response = client.get('/')
    assert b'Hello, World!' in response.data


def test_Tasks(client):
    response = client.get('/todo/api/v1.0/tasks')
    assert response.status_code == 200


def test_Task(client):
    response = client.get('/todo/api/v1.0/tasks/1')
    assert response.status_code == 200
