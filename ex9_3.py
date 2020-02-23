import requests
import json
import sys

N = sys.argv[1]
tagged = sys.argv[2]

url = 'https://api.stackexchange.com/2.2/questions?pagesize={}'\
      '&order=desc&sort=votes&tagged={}&site=stackoverflow'\
      .format(N, tagged)

resp = requests.get(url)
content = json.loads(resp.text)

message = ''
for i in content['items']:
    message += 'Title: {}\n'.format(i['title'])
    message += 'Link to top answer: https://stackoverflow.com/a/{}\n\n'\
               .format(i['accepted_answer_id'])

print(message)
