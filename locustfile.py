from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(0.1, 0.3)

    @task
    def my_task(self):
        self.client.get("/")