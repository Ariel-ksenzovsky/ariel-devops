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



# Question 1
### the purpose of the `Book` class is to holds the essential,
# information about a book, such as its title, author, and the number of copies available.

# the attributes that he have is title, author and copies. ###

### the purpose of the `library` class is to holds the essential,
# information about a books in the library, such as its title of books,
# authors, and the number of copies available in the library.

# the attributes that he have is only books that represents the the list of books in the library.###

# Question 2

### The add_book method in the Library class adds a Book object to the library's collection of books. 

# when the 'list_books' are called that print all added books from the method '.add_books'. ###

# Question 3

### The list_books method will print a list of all books that have been added to the Library object,
# the output will be list with title, autho and copies
# in that example the output will be: "Title: Python 101, Author: John Doe, Copies: 3
# Title: Data Science Handbook, Author: Jane Smith, Copies: 5"

# if we call `add_book` with a new book object that book added to the 'list_books',
# and when we call 'list_books' again we will see the new object ###


# Question 4
### efine a method in the Library class called find_book_by_title that takes a title as an argument.
# Iterate over the books list in the Library class.
# For each book, check if its title matches the provided title. ###