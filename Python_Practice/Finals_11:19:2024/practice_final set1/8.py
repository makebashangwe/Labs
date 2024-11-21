class Book:
    def __init__(self,title = None, author = None, pages = 0, read = False):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = read
    
    def print_details(self):
        print(f"Title: {self.title.capitalize()}\nAuthor: {self.author.capitalize()}\nPages: {self.pages}\nRead: {self.read}")
    def mark_read(self):
        if self.read == False:
            self.read = True
            print("You've marked this book as read.")
        elif self.read == True:
            unread = input("You've already marked this book as read.\nWould you like to unmark it?: ").lower()
            if "y" in unread:
                self.read = False
            else:
                return 


b1 = Book("Mink","Bitch",50,True)
b1.mark_read()
b1.print_details()

b2 = Book("Noodles","Po",3000,False)
b2.mark_read()
b2.print_details()

b2 = Book("Chicken recipies","ChicFilA",109,False)
b2.mark_read()
b2.print_details()