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