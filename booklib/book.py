import wget
from .settings import SOURCE, LIBRARY_IN, DIVIDER
from .utils import _notify
from .network_object import NetworkObject


class BookProps:
    ID = 0
    AUTHOR = 1
    TITLE = 2
    PUBLISHER = 3
    YEAR = 4
    PAGES = 5
    LANGUAGE = 6
    SIZE = 7
    _FORMAT = 8


class Book(NetworkObject):
    def __init__(self, book_metadata):
        _notify('BOOK metadata')
        _notify(book_metadata)
        self._id = book_metadata[BookProps.ID].text
        self.author = book_metadata[BookProps.AUTHOR].a.text
        self.title = book_metadata[BookProps.TITLE].a.text
        self.publisher = book_metadata[BookProps.PUBLISHER].text
        self.year = book_metadata[BookProps.YEAR].text
        self.pages = book_metadata[BookProps.PAGES].text
        self.language = book_metadata[BookProps.LANGUAGE].text
        self.size = book_metadata[BookProps.SIZE].text
        self._format = book_metadata[BookProps._FORMAT].text
        self.download_page = book_metadata[BookProps.TITLE].a.get('href')

    def __str__(self):
        return (
            f"[{self._id}] {self.title}\n by {self.author}\nFormat: {self._format}, size: {self.size}"
        )

    def get_download_link(self):
        dl_page_soup = self._fetch_soup(SOURCE + '/' + self.download_page)
        next_dl_page = dl_page_soup.find(
            'a', title='Gen.lib.rus.ec'
        ).get('href')
        _notify('next page')
        _notify(next_dl_page)
        if not next_dl_page:
            raise Exception('could not follow 1st download link')
        next_dl_soup = self._fetch_soup(next_dl_page)
        download_link = next_dl_soup.find('div', id='download')
        _notify(f'unproc dl link {download_link}')
        download_link = download_link.h2
        _notify(f'unproc 2 dl link {download_link}')
        download_link = download_link.a
        _notify(f'unproc 3 dl link {download_link}')
        download_link = download_link['href']
        _notify(download_link)
        return download_link

    def download(self):
        dl_link = self.get_download_link()
        wget.download(
            dl_link,
            f'/home/emil/Books/unsorted/{self.title}.{self._format}'
        )
