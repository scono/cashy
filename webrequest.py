import json
import requests

def google_search(query_string, nr_str):
    url = 'https://www.googleapis.com/customsearch/v1'
    key = '++++++ zu ergänzen +++++++'
    cx = '++++++ zu ergänzen +++++++'
    query = query_string

    search_str = ''

    for i in [1,11]:
        if i == 1:
            parameters = {"q": query,
                          "cx": cx,
                          "key": key,
                          "lr": "lang_de"
                         }
        else:
            parameters = {"q": query,
                          "cx": cx,
                          "key": key,
                          "lr": "lang_de",
                          "start": i
                         }

        page = requests.request("GET", url, params=parameters)
        data = json.loads(page.text)

        #for j in range(len(data['items'])):
        #    search_str += data["items"][j]["snippet"] + data["items"][j]["title"]
        search_str += str(data)

        #Zur Sicherheit wegspeichern
        path = r'C:\Users\Gottkönig\Desktop\cashshow\hist\\' + str(nr_str) + r'.txt'
        with open(path, 'w', encoding='utf-8') as outfile:
            outfile.write(search_str)

    return search_str
   

if __name__ == "__main__":
    pass