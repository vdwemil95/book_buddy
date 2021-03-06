from .utils import _notify
from urllib.error import HTTPError
from .book import Book
from .bookstore import BookStore
from .network_object import NetworkObject


SEARCH_QUERY = 'http://libgen.rs/search.php?req={query}&open=0&res=25&view=simple&phrase=1&column=def'
SOURCE = "http://libgen.rs"


class BookDataExtractor(NetworkObject):
    def __init__(self):
        pass

    def find_book(self, search_query, _format='pdf'):
        results = self._search(search_query)
        if not results:
            return None
        book_metadata = [self._parse_result(r) for r in results]
        result_bookstore = BookStore(book_metadata)
        result_bookstore.sort(_format=_format)
        return result_bookstore

    def _parse_result(self, book_soup):
        book_metadata = book_soup.find_all('td')
        _notify(book_metadata)
        book_metadata = book_metadata[:9]
        _notify(book_metadata)
        selected_book = Book(book_metadata)
        _notify(selected_book)
        return selected_book

    def _search(self, search_query):
        search_query = search_query.replace(' ', '+').lower()
        results = self._scrape_results(
            self._fetch_soup(SEARCH_QUERY.format(query=search_query))
        )
        return results

    def _scrape_results(self, soup):
        _notify('Extracting results')
        results = soup.find('table', class_='c')
        results = results.find_all('tr')[1:]
        num_results = len(results)
        _notify(f'Found {num_results} exact matches')
        return results

    # remove this
    # def download_book(self, search_term, _format):
    #     try:
    #         results = self.search(search_term)
    #         book_selection = [self._parse_result(r) for r in results]
    #         my_bookstore = BookStore(book_selection).sort(_format=_format)
    #     except Exception as e:
    #         print(e)
    #         exit(1)
    #     try:
    #         selected_book = my_bookstore.pop()
    #         print('Attempting to download the following book:\n')
    #         print(selected_book)
    #         selected_book.download()
    #     except HTTPError as e:
    #         print(e)
