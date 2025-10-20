class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
class EBook(Book):
    def __init__(self, title, author,file_size):
        self.file_size=file_size
        super().__init__(title, author)
    pass
class PrintBook(Book):
    def __init__(self, title, author,page_count):
        self.page_count=page_count
        super().__init__(title, author)
class Library:
    

    def __init__(self):
       # self.classic_book=Book(title,author)
        #self.digital_novel=EBook(title,author,file_size)
        #self.paper_novel=PrintBook(title,author,page_count)
        self.books=[]
    def add_book(self,book):    
        if isinstance(book,(Book,EBook,PrintBook)):
            self.books.append(book)
        else:
            raise TypeError("can only add Book,EBook,Printbook instances")
    def list_books(self):
            for book in self.books:
                if isinstance(book,EBook):
                    print(f"Title:{self.title},Author:{self.author}Format: EBook, File Size:{self.page_count}")
                elif isinstance(book, PrintBook):
                    print(f"Title: {book.title}, Author: {book.author}, Format: Print, Pages: {book.page_count}")
                elif isinstance(book, Book):
                    print(f"Book: {book.title} by {book.author}")    
                
                
            else:
                print(f"Title: {book.title}, Author: {book.author}, Format: Unknown")     


