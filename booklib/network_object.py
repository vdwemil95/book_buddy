from .utils import _notify
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests


class NetworkObject:
    def _fetch_soup(self, endpoint):
        _notify(f'Fetching soup page {endpoint}')
        source = requests.get(endpoint).text
        return BeautifulSoup(source, 'lxml')
