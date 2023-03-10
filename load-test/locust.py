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
        self.client.post('/cmcd/media/vod/bbb_30fps_akamai/bbb_30fps_320x180_400k/bbb_30fps_320x180_400k_0.m4v?CMCD=cid%3D%2221cf726cfe3d937b5f974f72bb5bd06a%22%2Cot%3Di%2Csf%3Dd%2Csid%3D%225a16d9dd-ca72-4c0c-9eb9-b013815060bb%22%2Cst%3Dv%2Csu', json=params)
