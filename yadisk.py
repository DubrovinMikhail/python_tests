import os
import requests


class YaUploader:
    token = os.getenv("TOKEN")
    host = "https://cloud-api.yandex.net:443"
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}

    def __init__(self, token: str):
        self.token = token

    def dir_inst(self, name):
        url = f'{self.host}/v1/disk/resources'
        params = {'path': name}
        requests.put(url, params=params, headers=YaUploader.headers)


uploader = YaUploader(YaUploader.token)
if __name__ == '__main__':
    uploader.dir_inst("test_dir")