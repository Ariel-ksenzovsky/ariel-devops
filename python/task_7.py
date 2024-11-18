import math


class Book:
 def __init__(self, title, author, copies):
    self.title = title
    self.author = author
    self.copies = copies
    
 def __str__(self):
    return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

harry_potter = Book('harry poter', 'ariel', 1500000)
str(harry_potter)

class Library:
 def __init__(self):
    self.books = []
    
 def add_book(self, book):
    self.books.append(book)
    
 def list_books(self):
    for book in self.books:
        print(book)
books = []
author = {'ariel': [], 'emil': []}


def get_last_book_from_author(): pass



        
# Example Usage
library = Library()
learn_python_book = Book("Python 101", "John Doe", 3)
library.add_book(learn_python_book)
library.add_book(Book("Data Science Handbook", "Jane Smith", 5))
library.list_books()