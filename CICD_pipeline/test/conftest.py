import sys
sys.path.insert(0, 'D:\Github\LearnDevOps\CICD_pipeline\code')

import pytest
from app import app as flask_app
@pytest.fixture
def app():
    yield flask_app
@pytest.fixture
def client(app):
    return app.test_client()