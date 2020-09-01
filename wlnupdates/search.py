#Python file for searching novels by string and exporting ID
import requests
import sys
import json
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

    def search_advanced(self, name=None, tag_category=None, genre_category=None, chapter_limits=None, series_type=None, sort_mode=None):
        payload = {"mode": "search-advanced"}
        if name:
            payload['title-search-text'] = name
        elif tag_category:
            payload['tag-category'] = tag_category
        elif genre_category:
            payload['genre-category'] = genre_category
        elif chapter_limits:
            payload['chapter-limits'] = chapter_limits
        elif series_type:
            payload['series-type'] = series_type
        elif sort_mode:
            payload['sort-mode'] = sort_mode
        payload = json.dumps(payload)
        print(str(payload))




        test = { 'mode' : 'search-advanced', 'series-type' : {'Translated' : 'included'}, 'tag-category' : { 'ability-steal' : 'included', 'virtual-reality' : 'excluded' }, 'sort-mode' : "update", 'chapter-limits' : [40, 0], }

        


        response = requests.request("POST", self.url, headers=self.headers, data="'"+json.dumps(test)+"'")
        return response
    

test = Search()

print(test.search_advanced(series_type={'Translated' : 'included'}, tag_category={ 'ability-steal' : 'included', 'virtual-reality' : 'excluded' }))