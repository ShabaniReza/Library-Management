from locust import HttpUser, task, between
from random import randint

class BooksEndpoint(HttpUser):
    wait_time = between(1, 5)

    task(2)
    def view_books(self):
        self.client.get('/library/books/', name='View books')

    task(1)
    def view_book(self):
        book_id = randint(1, 20)
        self.client.get(f'/library/books/{book_id}/', name='View a book')