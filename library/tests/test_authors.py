from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestCreateAuthor:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        client = APIClient()
        response = api_client.post('/library/authors/', {'first_name': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED