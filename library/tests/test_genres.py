from rest_framework import status
from model_bakery import baker
from library.models import Genre
import pytest


# ! ____________________________Fixtures____________________________

@pytest.fixture
def create_genre(api_client):
    def do_create_genre(genre_information):
        return api_client.post('/library/genres/', genre_information)
    return do_create_genre

# ! ____________________________Create____________________________

@pytest.mark.django_db
class TestCreateGenre:
    def test_if_user_is_anonymous_returns_401(self, create_genre):
        response = create_genre({'name': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_genre):
        authenticate()

        response = create_genre({'name': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_returns_201(self, authenticate, create_genre):
        authenticate(True)

        response = create_genre({'name': 'a'})

        assert response.status_code == status.HTTP_201_CREATED

    def test_is_data_is_invalid_returns_400(self, authenticate, create_genre):
        authenticate(True)

        response = create_genre({'name': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['name'] is not None

# ! ____________________________Retrieve____________________________

@pytest.mark.django_db
class TestRetrieveGenre:
    def test_if_genre_exist_returns_200(self, api_client):
        genre = baker.make(Genre)

        response = api_client.get(f'/library/genres/{genre.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': genre.id,
            'name': genre.name
        }