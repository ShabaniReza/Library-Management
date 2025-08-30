from rest_framework import status
from model_bakery import baker
from library.models import Author
import pytest


# ! Fixtures 

@pytest.fixture
def create_author(api_client):
    def do_create_author(author_information):
        return api_client.post('/library/authors/', author_information)
    return do_create_author

@pytest.fixture
def patch_author(api_client):
    def do_patch_author(author_information, author_id):
        return api_client.patch(f'/library/authors/{author_id}/', author_information)
    return do_patch_author

# ! ____________________________Create____________________________

@pytest.mark.django_db
class TestCreateAuthor:
    def test_if_user_is_anonymous_returns_401(self, create_author):
        response = create_author({'first_name': 'a', 'last_name': 'b'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_author):
        authenticate()

        response = create_author({'first_name': 'a', 'last_name': 'b'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_returns_201(self, authenticate, create_author):
        authenticate(True)

        response = create_author({'first_name': 'a', 'last_name': 'b'})

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_returns_400(self, authenticate, create_author):
        authenticate(True)

        response = create_author({'first_name': '', 'last_name': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['first_name'] is not None
        assert response.data['last_name'] is not None

# ! ____________________________Retrieve____________________________

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
    
    def test_if_author_not_exists_returns_404(self, api_client):
        id = 9999

        response = api_client.get(f'/library/authors/{id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

# ! ____________________________List____________________________

@pytest.mark.django_db
class TestListAuthor:
    def test_if_authors_exists_returns_200(self, api_client):
        authors = baker.make(Author, _quantity=5)

        response = api_client.get(f'/library/authors/')

        assert response.status_code == status.HTTP_200_OK

# ! ____________________________Patch____________________________

@pytest.mark.django_db
class TestPatchAuthor:
    def test_if_user_is_anonymous_returns_401(self, patch_author):
        author = baker.make(Author)

        response = patch_author({'first_name': 'a'}, author.id)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, patch_author):
        author = baker.make(Author)
        authenticate()

        response = patch_author({'first_name': 'a'}, author.id)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_returns_200(self, authenticate, patch_author):
        author = baker.make(Author)
        authenticate(True)

        response = patch_author({'first_name': 'a'}, author.id)

        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_invalid_returns_400(self, authenticate, patch_author):
        author = baker.make(Author)
        authenticate(True)

        response = patch_author({'first_name': ''}, author.id)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['first_name'] is not None