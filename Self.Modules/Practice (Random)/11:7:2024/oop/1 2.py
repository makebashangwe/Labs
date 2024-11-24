class Book:
    def __init__(self, title = "", author = "", pages = 0): #none more effetive
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_details(self):
        print(self.title.title())
        print(self.author.title())
        print(self.pages)
    
    def checkpages(self):
        if self.pages > 300:
            print("Contains over 300 pages!")
        else:
            print(f"{self.title.title()} contains {self.pages} pages.")


# Create instances of Book with different data
book1 = Book("the great gatsby", "f. scott fitzgerald", 180)
book2 = Book("war and peace", "leo tolstoy", 1225)
book3 = Book("1984", "george orwell", 328)

# Test display_details method
print("Testing display_details method:")
book1.display_details()  # Expected: Title and author capitalized, printed once each
print("---")
book2.display_details()  # Expected: Title and author capitalized, printed once each
print("---")
book3.display_details()  # Expected: Title and author capitalized, printed once each

# Test checkpages method
print("\nTesting checkpages method:")
book1.checkpages()  # Expected: "The Great Gatsby contains 180 pages."
book2.checkpages()  # Expected: "Contains over 300 pages!"
book3.checkpages()  # Expected: "Contains over 300 pages!"
