from rest_framework import status
from model_bakery import baker
from library.models import Author
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

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_author):
        authenticate()

        response = create_author({'first_name': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
class TestRetrieveAuthor:
    def test_if_author_exists_returns_200(self, api_client):
        author = baker.make(Author)

        response = api_client.get(f'/library/authors/{author.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': author.id,
            'first_name': author.first_name,
            'last_name': author.last_name,
            'date_of_birth': author.date_of_birth,
            'date_of_death': author.date_of_death,
            'biography': author.biography
        }