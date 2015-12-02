import urllib
from bs4 import BeautifulSoup


def scrap():
    url ="http://haithemabdelli.com/"
    response = urllib.urlopen(url)
    htmltext = BeautifulSoup(response, "html.parser")
    text = htmltext.find('div',{'class':'carousel-content'}).text
    return text