import json
import os
import requests

class API:

    def __init__(self, base_url):
        self.base_url = base_url

    
    def get_data(self, path):
        """
        return : dictionary of data
        """
        self.path = path
        self.url = os.path.join(self.base_url, path)
        self.r = requests.get(self.url)
        data = json.loads(self.r.text)
        return data



