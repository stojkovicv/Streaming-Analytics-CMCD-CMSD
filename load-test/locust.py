from locust import HttpUser, task, between

class CMCDUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def send_cmcd_logs(self):
        self.client.get('/cmcd/media/vod/bbb_30fps_akamai/bbb_30fps_320x180_400k/bbb_30fps_320x180_400k_0.m4v?CMCD=cid%3D%2221cf726cfe3d937b5f974f72bb5bd06a%22%2Cot%3Di%2Csf%3Dd%2Csid%3D%225a16d9dd-ca72-4c0c-9eb9-b013815060bb%22%2Cst%3Dv%2Csu')
