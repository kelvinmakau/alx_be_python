class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class EBook(Book): #Inherits attributes from the initial Book class i.e title and author, the adds file_size
    def __init__(self, title, author, file_size):
        super().__init__(title, author) # calls Book's __init__
        self.file_size = file_size

class PrintBook(Book): #Inherits attributes from the initial Book class i.e title and author, the adds page_count
    def __init__(self, title, author, page_count ):
        super().__init__(title, author) # calls Book's __init__
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        # looping through each collection
        for book in self.books:
            if isinstance(book, EBook):
                print(f"Ebook: {book.title} by {book.author}, File Size: {book.file_size}KB")

            if isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, File Size: {book.page_count}")

            else:
                print(f"Book: {book.title} by {book.author}")