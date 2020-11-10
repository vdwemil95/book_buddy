from .book import Book
from .settings import *
from .utils import _notify


class BookStore():
    def __init__(self, book_list):
        self.books = book_list

    def sort(self, _format='pdf'):
        self.books = [book for book in self.books if book._format == _format]

    def pop(self):
        if not self.has_books:
            raise Exception('no books!')
        return self.books.pop(0)

    def has_books(self):
        return len(self.books) > 0

    def __str__(self):
        if not self.has_books():
            return 'The shelves are empty'
        book_store_str = self.books[0].__str__()
        for book in self.books[1:]:
            book_store_str += DIVIDER + book.__str__() + DIVIDER
        return book_store_str
