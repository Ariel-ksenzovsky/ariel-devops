class Book:
   
 def __init__(self, title, author, copies):
   self.title = title
   self.author = author
   self.copies = copies
 
 def __str__(self):
   return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"


class Library:

 def __init__(self):
   self.books = []

 def add_book(self, book):
   self.books.append(book)

 def list_books(self):
   for book in self.books:
      print(book)
# Example Usage
library = Library()
library.add_book(Book("Python 101", "John Doe", 3))
library.add_book(Book("Data Science Handbook", "Jane Smith", 5))
library.list_books()