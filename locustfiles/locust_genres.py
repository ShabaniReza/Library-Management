from locust import HttpUser, task, between

class GenresEndpoint(HttpUser):
    wait_time = between(1, 5)

    @task()
    def view_genres(self):
        self.client.get('/library/genres/', name='View genres')