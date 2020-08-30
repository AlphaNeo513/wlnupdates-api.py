#Python file for searching novels by string and exporting ID
import requests
from pprint import pprint
class Search:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'} 
        self.url = "https://www.wlnupdates.com/api" #API link


    def title_search(self, name, similarityNum=0, fullList=False): #similarityNum is the variable for finding how big of a similarity
            payload = '{"title": "'+name+'", "mode": "search-title"}'
            response = requests.request("POST", self.url, headers=self.headers, data=payload)
            json_data = response.json()
            json_data = json_data['data']['results']
            if fullList is True:
                idList = []                
                for results in json_data:
                    if results['match'][0][0] >= similarityNum:
                        idList.append(results)
                
                return idList

            else:
                pprint(json_data)


test = Search()

print(test.title_search('The Book Eating Magician', similarityNum=0, fullList=True))