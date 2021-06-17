import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')#pegando informacoes do site
soup = BeautifulSoup(res.text,'html.parser')#transformar em html
links = soup.select('.storylink')
#votes = soup.select('.score')
subtext = soup.select('.subtext')

'''
def create_custem_hn(links, votes):
    hn=[]
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href', None)
        hn.append({'title':title, 'links':href})
    return hn
print(create_custem_hn(links, votes))
'''

'''
#adicionar votes 
def create_custem_hn(links, subtext):
    hn=[] #criar lista
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href', None)
        vote = subtext[inx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title':title, 'links':href, 'votes':points})
    return hn
pprint.pprint(create_custem_hn(links, subtext))
'''

#usando sort 
def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'])

def create_custem_hn(links, subtext):
    hn=[] #criar lista
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href', None)
        vote = subtext[inx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title':title, 'links':href, 'votes':points})
    return sort_stories_by_vote(hn)
pprint.pprint(create_custem_hn(links, subtext))