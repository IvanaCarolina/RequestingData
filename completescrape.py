import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/') #pegando informacoes do site
res2 = requests.get('https://news.ycombinator.com/news?p=2') #segunda pag

soup = BeautifulSoup(res.text,'html.parser') #transformar em html
soup2 = BeautifulSoup(res2.text,'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')

links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

#usando sort 
def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'],reverse=True)

def create_custem_hn(links, subtext):
    hn=[] #criar lista
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href', None)
        vote = subtext[inx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            #if points > 99:
            hn.append({'title':title, 'links':href, 'votes':points})
    return sort_stories_by_vote(hn)
pprint.pprint(create_custem_hn(mega_links,mega_subtext))