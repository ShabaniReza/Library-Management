from locust import HttpUser, task, between

class BooksEndpoint(HttpUser):
    wait_time = between(1, 5)

    def view_books(self):
        self.client.get('/library/books/', name='View books')