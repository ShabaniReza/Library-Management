from locust import HttpUser, task, between
from random import randint

class AuthorsEndpoint(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_authors(self):
        self.client.get('/library/authors/', name='View authors')
        
    @task(1)
    def view_author(self):
        author_id = randint(1, 20)
        self.client.get(f'/library/authors/{author_id}/', name='View an author')