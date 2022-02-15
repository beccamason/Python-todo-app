import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client(): 
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client: 
        yield client

