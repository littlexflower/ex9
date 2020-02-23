import requests
import sys
from bs4 import BeautifulSoup

url = 'http://ketqua.net/'
arg = sys.argv[1:]
check = 0
message = ''

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

tags = soup.find_all('td', id=lambda i: i and i.startswith('rs_'))
results = [i.text for i in tags]

for i in results:
    for j in arg:
        if int(i[-2:]) == int(j):
            message = 'Chuc mung ban da trung con lo {}'.format(j)
            check += 1

if check == 0:
    message = 'Chuc ban may man lan sau.\n'
    message += 'Ket qua xo so la:\n'
    message += '\n'.join(results)

print(message)
