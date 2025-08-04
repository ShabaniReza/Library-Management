from rest_framework import status
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def create_author(api_client):
    def do_create_author(author_information):
        return api_client.post('/library/authors/', author_information)
    return do_create_author


@pytest.mark.django_db
class TestCreateAuthor:
    def test_if_user_is_anonymous_returns_401(self, create_author):
        response = create_author({'first_name': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED