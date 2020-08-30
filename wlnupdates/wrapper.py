import requests
from pprint import pprint
url = "https://www.wlnupdates.com/api"
payload = '{"id": 45094, "mode": "get-series-id"}'
#payload = '{"title": "The Book Eating Magician", "mode": "search-title"}'
headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data = payload)
json_data = response.json()
class Request:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'} 
        self.url = "https://www.wlnupdates.com/api" #API link


    def get_series_data(self, id):
            payload = '{"id":'+ id +', "mode": "get"}'
            response = requests.request("POST", self.url, headers=self.headers, data=payload)
            json_data = response.json()
            if json_data['error'] is True:
                print('Error! '+json_data['message'])
            else:
                return json_data
data = Request()


pprint(data.get_series_data('3'))