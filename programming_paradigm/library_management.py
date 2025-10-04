class Book:
    def __init__(self, title, author):
        """
        Initialize a Book with title, author, and availability status.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title  # public attribute
        self.author = author  # public attribute
        self._is_checked_out = False  # private attribute
    
    def check_out(self):
        """Check out the book if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Return the book if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book."""
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self._books = []  # private list to store Book instances
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): A Book instance to add to the library
        """
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added book: '{book.title}' by {book.author}")
        else:
            print("Error: Can only add Book instances to the library.")
    
    def check_out_book(self, title):
        """
        Check out a book by title.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if successful, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"Successfully checked out: '{book.title}'")
                    return True
                else:
                    print(f"Book '{book.title}' is already checked out")
                    return False
        print(f"Book with title '{title}' not found in library")
        return False
    
    def return_book(self, title):
        """
        Return a book by title.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if successful, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"Successfully returned: '{book.title}'")
                    return True
                else:
                    print(f"Book '{book.title}' was not checked out")
                    return False
        print(f"Book with title '{title}' not found in library")
        return False
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No available books in the library")
            return
        
        print("Available Books:")
        for i, book in enumerate(available_books, 1):
            print(f"{i}. '{book.title}' by {book.author}")
    
    def find_book(self, title):
        """
        Find a book by title (case-insensitive).
        
        Args:
            title (str): The title to search for
            
        Returns:
            Book or None: The book if found, None otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None


# Demonstration of the Library Management System
if __name__ == "__main__":
    # Create a library
    library = Library()
    
    # Add some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    print("\n" + "="*50 + "\n")
    
    # List available books
    library.list_available_books()
    
    print("\n" + "="*50 + "\n")
    
    # Test checking out books
    library.check_out_book("The Great Gatsby")
    library.check_out_book("1984")
    
    print("\n" + "="*50 + "\n")
    
    # List available books after checkouts
    library.list_available_books()
    
    print("\n" + "="*50 + "\n")
    
    # Test returning a book
    library.return_book("The Great Gatsby")
    
    print("\n" + "="*50 + "\n")
    
    # List available books after return
    library.list_available_books()
    
    print("\n" + "="*50 + "\n")
    
    # Test edge cases
    library.check_out_book("Unknown Book")  # Book not found
    library.return_book("To Kill a Mockingbird")  # Book not checked out
    library.check_out_book("The Great Gatsby")  # Check out again