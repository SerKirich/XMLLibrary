from booklib import *
import sys

lib = ParseBooks()

while True:
    try:
        cmd = input("> ")
    except:
        sys.exit()
    if cmd == "all":
        for book in lib.booklist:
            book.Print()
    if cmd.find("book ") != -1:
        found = lib.GetBooksByTitle(cmd.partition("book ")[2])
        for book in found:
            book.Print()
    if cmd.find("author ") != -1:
        found = lib.GetBooksByAuthor(cmd.partition("author ")[2])
        for book in found:
            book.Print()
    if cmd.find("genre ") != -1:
        found = lib.GetBooksByGenre(cmd.partition("genre ")[2])
        for book in found:
            book.Print()
    if cmd.find("description ") != -1:
        found = lib.GetBooksByDescription(cmd.partition("description ")[2])
        for book in found:
            book.Print()
