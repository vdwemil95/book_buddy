import requests
from bs4 import BeautifulSoup
import wget
from enum import Enum
import urllib.request
from urllib.error import HTTPError
from .settings import *
from .book import Book
from .bookstore import BookStore
from .utils import *


def auto_download():
    for book, _format in my_book_list:
        search_query = book
        results = search(search_query)
        book_selection = [parse_result(r) for r in results]
        my_bookstore = BookStore(book_selection).sort(_format=_format)
        try:
            selected_book = my_bookstore.pop()
            selected_book.download()
        except HTTPError as e:
            print(e)




   

def get_user_confirmation(book):
    print(book.title)
    print(f'Format: {book._format}')
    return input('Download this book? [y/n]') == 'y'



