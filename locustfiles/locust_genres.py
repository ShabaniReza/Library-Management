from locust import HttpUser, task, between
from random import randint

class GenresEndpoint(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_genres(self):
        self.client.get('/library/genres/', name='View genres')

    @task(1)
    def view_genre(self):
        genre_id = randint(1, 20)
        self.client.get(f'/library/genres/{genre_id}/', name='View a genre')