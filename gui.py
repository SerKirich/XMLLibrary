from booklib import *
from tkinter import *

lib = ParseBooks()

class BookWindow:
    """BookWindow class"""
    def __init__(self, title):
        self.book = lib.GetBooksByTitle(title)[0]

        self.window = Tk()
        self.window.title(title)
        self.window.geometry("640x480")

        self.window_title = Label(self.window, width = 30, height = 1, text = self.book.title)
        self.window_author = Label(self.window, width = 30, height = 1, text = self.book.author)
        self.window_genre = Label(self.window, width = 30, height = 1, text = self.book.genre)
        self.window_descr = Label(self.window, width = 64, height = 10, text = self.book.description)

        self.window_title.pack()
        self.window_author.pack()
        self.window_genre.pack()
        self.window_descr.pack()

class Root:
    """Root window class"""
    def __init__(self):

        self.window = Tk()
        self.window.title("Library")
        self.window.geometry("700x400")
        self.window.resizable(False,False)

        self.entry_frame = Frame(self.window)
        self.entry_label = Label(self.entry_frame, width = 8, height = 1, text = "Search:")
        self.entry = Entry(self.entry_frame, width = 32)

        self.result_frame = Frame(self.window)
        self.result = Text(self.result_frame, width = 32, height = 16)
        self.result.config(state = "disabled")

        self.entry_frame.pack()
        self.entry_label.pack()
        self.entry_label.pack()
        self.entry.pack()

        self.result_frame.pack()
        self.result.pack()

        def FindBook(event):
            cmd = self.entry.get()
            self.entry.delete("0",END)
            if cmd == "all":
                self.result.config(state = "normal")
                self.result.delete("1.0",END)
                for book in lib.booklist:
                    self.result.insert(END,book.title)
                    self.result.insert(END,"\n")
                self.result.config(state = "disabled")
            if cmd.find("book ") != -1:
                self.result.config(state = "normal")
                self.result.delete("1.0",END)
                found = lib.GetBooksByTitle(cmd.partition("book ")[2])
                for book in found:
                    self.result.insert(END,book.title)
                    self.result.insert(END,"\n")
                self.result.config(state = "disabled")
            if cmd.find("author ") != -1:
                self.result.config(state = "normal")
                self.result.delete("1.0",END)
                found = lib.GetBooksByAuthor(cmd.partition("author ")[2])
                for book in found:
                    self.result.insert(END,book.title)
                    self.result.insert(END,"\n")
                self.result.config(state = "disabled")
            if cmd.find("genre ") != -1:
                self.result.config(state = "normal")
                self.result.delete("1.0",END)
                found = lib.GetBooksByGenre(cmd.partition("genre ")[2])
                for book in found:
                    self.result.insert(END,book.title)
                    self.result.insert(END,"\n")
                self.result.config(state = "disabled")
            if cmd.find("description ") != -1:
                self.result.config(state = "normal")
                self.result.delete("1.0",END)
                found = lib.GetBooksByDescription(cmd.partition("description ")[2])
                for book in found:
                    self.result.insert(END,book.title)
                    self.result.insert(END,"\n")
                self.result.config(state = "disabled")
            if cmd.find("open ") != -1:
                BookWindow(cmd.partition("open ")[2])

        self.entry.bind("<Return>",FindBook)
