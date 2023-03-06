from locust import HttpUser, task, between

class StreamingUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def cmcd_server(self):
        self.client.get("http://localhost:5500/stream-client/", stream=True)