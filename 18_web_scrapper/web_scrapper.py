import requests
from bs4 import BeautifulSoup

url = ''

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

title = soup.find_all('h2', {'class': 'post-title'})

title.gettext()

title1 = title[0].gettext()

for t in title:
    print(t.gettext())
