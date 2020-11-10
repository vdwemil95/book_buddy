from booklib.book_data_extractor import BookDataExtractor


def main():
    book_de = BookDataExtractor()
    result_bookstore = book_de.find_book(
        search_query=input('Enter a search term: '),
        _format=input('Book format [epub, pdf]: ')
    )
    while result_bookstore.has_books():
        candidate = result_bookstore.pop()
        print(candidate)
        if input('Download this book?') == 'y':
            candidate.download()
            break


main()
