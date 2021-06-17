import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')#pegando informacoes do site
soup = BeautifulSoup(res.text,'html.parser')#transformar em html
links = soup.select('.storylink')
votes = soup.select('.score')


def create_custem_hn(links, votes):
    hn=[]
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href', None)
        hn.append({'title':title, 'links':href})
    return hn
print(create_custem_hn(links, votes))