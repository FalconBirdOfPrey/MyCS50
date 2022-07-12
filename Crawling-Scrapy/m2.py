import requests
import re
import lxml.html
from bs4 import BeautifulSoup

def extractLinkRegEx(txt):
    tgs = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)
    return [match[1] for match in tgs.findall(txt)]

def extractLinksLxml(txt):
    lst = []
    dom = lxml.html.fromstring(txt)
    for l in dom.xpath('//a/@href'):
        lst.append(l)
    return lst    

def extractBs(txt):
    lst = []
    s = BeautifulSoup(txt, 'lxml')
    for tag in s.find_all('a', href=True):
        lst.append(tag['href'])
    return lst    


def printList(lst):
    for l in lst:
        print('Level 1 -> ' + l)

r = requests.get('https://www.folkhalsomyndigheten.se/')
#print(extractLinkRegEx(r.text)
#printList(extractLinkRegEx(r.text))
#printList(extractLinksLxml(r.text))
printList(extractsBs(r.text))

