from locust import HttpUser, task, between

class CMCDUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def send_cmcd_logs(self):
        params = {
            "sf": "d",
            "time": "2023-02-14T14:26:06+00:00",
            "d": "4000",
            "st": "v",
            "rtp": "5000",
            "br": "4952",
            "nor": "bbb_30fps_1280x720_4000k_8.m4v",
            "bl": "20200",
            "cid": "21cf726cfe3d937b5f974f72bb5bd06a",
            "sid": "3a799169-87c9-40bd-bc8f-cf7aacdb2a79",
            "mtp": "587100",
            "dl": "20200",
            "ot": "v",
            "bs": "true",
            "su": "false"
            }
        self.client.post('/cmcd-bridge', json=params)
