from xml.dom import minidom

class Book:
    """Book class."""
    def __init__(self, title, author, genre, description):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
    def Print(self):
        print(
        "Book: {}\nAuthor: {}\nGenre: {}\nDescription: {}".format(self.title,self.author,self.genre,self.description)
        )

class Library:
    """Library class."""
    def __init__(self, booklist):
        self.booklist = booklist
    def GetBooksByTitle(self, title):
        found = []
        for book in self.booklist:
            if book.title.upper().find(title.upper()) != -1:
                found.append(book)
        return found
    def GetBooksByAuthor(self, author):
        found = []
        for book in self.booklist:
            if book.author.upper().find(author.upper()) != -1:
                found.append(book)
        return found
    def GetBooksByGenre(self, genre):
        found = []
        for book in self.booklist:
            if book.genre.upper().find(genre.upper()) != -1:
                found.append(book)
        return found
    def GetBooksByDescription(self, description):
        found = []
        for book in self.booklist:
            if book.description.upper().find(description.upper()) != -1:
                found.append(book)
        return found

def ParseBooks():
    doc = minidom.parse("books.xml")
    doc_books = doc.getElementsByTagName("book")
    books = []

    for doc_book in doc_books:
        doc_book_tit = doc_book.getElementsByTagName("title")[0].firstChild.nodeValue
        doc_book_aut = doc_book.getElementsByTagName("author")[0].firstChild.nodeValue
        doc_book_gen = doc_book.getElementsByTagName("genre")[0].firstChild.nodeValue
        doc_book_des = doc_book.getElementsByTagName("description")[0].firstChild.nodeValue
        books.append(Book(doc_book_tit,doc_book_aut,doc_book_gen,doc_book_des))

    lib = Library(books)
    return lib
