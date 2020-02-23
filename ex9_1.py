import requests
import sys
import json

url = 'https://api.github.com/users/' + sys.argv[1] + '/repos'

resp = requests.get(url)
content = json.loads(resp.text)
for i in content:
    print(i['name'])
