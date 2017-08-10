from bs4 import BeautifulSoup
import urllib.request


class Scraping:
    def __init__(self, url="https://github.com"):
        self._url = url
        html = urllib.request.urlopen(self._url)
        self._soup = BeautifulSoup(html, "html.parser")

    def set_url(self, _url):
        self._url = _url
        html = urllib.request.urlopen(self._url)
        self._soup = BeautifulSoup(html, "html.parser")

if __name__ == "__main__":
    sc = Scraping()
