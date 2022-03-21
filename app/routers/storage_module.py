import json

import requests


class Storage:
    def __init__(self, url):
        self.url = url

    def create_file(self, filename: str, file_data: str):
        response = requests.post(
            url=f'{self.url}/create_file',
            params={
                'filename': filename,
                'file_data': file_data
            }
        )
        return response.status_code

    def delete_file(self, filename):
        response = requests.post(
            url=f'{self.url}/delete_file',
            params={
                'filename': filename,
            }
        )
        return response.status_code

    def download_file(self, filename: str):
        response = requests.get(
            url=f'{self.url}/download_file',
            params={
                'filename': filename,
            }
        )
        return response.content

    def list_files(self):
        response = requests.get(
            url=f'{self.url}/list_files',
        )
        return json.loads(response.content)[0]['files']

    def upload_file(self, f):
        response = requests.post(
            url=f'{self.url}/upload_file',
            params={
                'file': f,
            }
        )
        return response.status_code
