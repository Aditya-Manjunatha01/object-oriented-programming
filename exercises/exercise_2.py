"""
Exercise 2: Library and Books
A library has a collection of books. Each book has a title, an author, and a number of pages. The library has a name and can hold multiple books.
The library should be able to:

Add a book to its collection
Display all books it currently has
Find and return a book by its title
"""
import hashlib

class Book():
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    
class Library():
    def __init__(self, name) :
        self.name = name
        # Im keeping books_collection as a dictionary of the books the library has right now
        # Elements of this collection will be list of  book objects (list to acount for the fact that multiple books can have the same name)
        self.books_collection = {} 

    def generate_id(self, title: str):
        # Takes the name of the book as input and gives it an id
        title_normalized = title.lower()
        book_id = hashlib.md5(title_normalized.encode('utf-8')).hexdigest()
        return book_id

    def add_book(self, book):
        # book is an object which has to be passed to this method
        # No need to add self.book as its not an attribute of the library class 
        book_id = self.generate_id(book.title)

        # What to do if this book is already in the collection
        if book_id in self.books_collection.keys():
            # Check if author is distinct
            # 1) Gather all books with this title
            common_book_titles = self.books_collection[book_id] # Returns a list of book objects which have the same book_id(ie title name)
            # 2) Get the author names
            author_names = set()
            for book_obj in common_book_titles:
                author_names.add(book_obj.author)
            # 3) Check whether it exists in there
            if book.author in author_names:
                # Duplicated book
                print(f"Book already exists!")
            else:
                self.books_collection[book_id].append(book)
                print(f"Added {book.title} with author {book.author} to the collection successfully")
        else:
            # Going to keep the key as the book name and the value as the list of book objects 
            self.books_collection[book_id] = [book]
            print(f"Added {book.title} to the collection successfully")

    def show_all_books(self):

        for book_id in self.books_collection:
            num_books_same_title = len(self.books_collection[book_id])
            for i in range(num_books_same_title):
                print(f"Title : {self.books_collection[book_id][i].title}, Author : {self.books_collection[book_id][i].author}, Number of Pages : {self.books_collection[book_id][i].num_pages}")

    def find_book(self, title : str):
        # Search for title in the keys of book_collection
        book_id = self.generate_id(title)
        if book_id in self.books_collection.keys():
            # Found the book(s), return the list of book object(s)
            return self.books_collection[book_id]
        else :
            print(f"The book titled '{title}' is not part of the library")


if __name__ == '__main__' : 
    my_library = Library("Aditya's Library")
    my_book = Book("Machine Learning for Beginners", "Aditya", 100)

    my_library.add_book(my_book)
    my_library.show_all_books()
    my_library.find_book(input(f"Enter the title of the book you want to find: "))