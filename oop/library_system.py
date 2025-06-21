# Base class representing a generic book
class Book:
    def __init__(self, title, author):
        # Initialize the book's title and author
        self.title = title
        self.author = author

    def __str__(self):
        # Defines how the Book instance is printed
        return f"Book: {self.title} by {self.author}"


# Derived class representing an electronic book
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the constructor of the base class to set title and author
        super().__init__(title, author)
        # Initialize the EBook-specific attribute: file size in KB
        self.file_size = file_size

    def __str__(self):
        # Defines how the EBook instance is printed
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class representing a physical printed book
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the constructor of the base class to set title and author
        super().__init__(title, author)
        # Initialize the PrintBook-specific attribute: page count
        self.page_count = page_count

    def __str__(self):
        # Defines how the PrintBook instance is printed
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Class representing a library that contains books
class Library:
    def __init__(self):
        # Create an empty list to store book instances (composition)
        self.books = []

    def add_book(self, book):
        # Add a Book, EBook, or PrintBook instance to the library
        self.books.append(book)

    def list_books(self):
        # Print the string representation of each book using __str__
        for book in self.books:
            print(book)
