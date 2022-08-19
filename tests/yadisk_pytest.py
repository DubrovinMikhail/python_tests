import os
import yadisk
import requests

class Test_Uplouder:
    token = yadisk.YaUploader.token
    host = yadisk.YaUploader.host
    url = f'{host}/v1/disk/resources'
    def test_response(self):
        params = {'path': "/"}
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {Test_Uplouder.token}'}
        response = requests.get(Test_Uplouder.url, params=params, headers=headers).status_code
        assert response == 200

    def test_uploader(self):
        href = "https://cloud-api.yandex.net:443"
        name_dir = "test_dir"
        uploader = yadisk.YaUploader(os.getenv("TOKEN"))
        uploader.dir_inst(name_dir)
        url = f'{yadisk.YaUploader.host}/v1/disk/resources'
        params = {'path': '/'}
        response = requests.get(url, params=params, headers=yadisk.YaUploader.headers).json()
        name_list = [a["name"] for a in [items for items in response["_embedded"]["items"]]]
        assert name_dir in name_list
