class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return "Book already borrowed"
        self.is_borrowed = True
        return "You borrowed the book"

    def return_book(self):
        if not self.is_borrowed:
            return "Book is not borrowed"
        self.is_borrowed = False
        return "You returned the book"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            return "Borrow limit reached"
        if book in self.borrowed_books:
            return "Book already borrowed by this member"
        if book.is_borrowed:
            return "Book already borrowed by someone else"
        self.borrowed_books.append(book)
        book.borrow()
        return "Book borrowed successfully"

    def return_book(self, book):
        if book not in self.borrowed_books:
            return "Book not borrowed by this member"
        self.borrowed_books.remove(book)
        book.return_book()
        return "Book returned successfully"