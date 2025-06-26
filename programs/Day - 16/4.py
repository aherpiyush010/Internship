# Create a Book Class
# Attributes:
# title, author, year.
# Method:
# get_description() — Returns a formatted description like:
# "The book 'Title' by Author was published in Year."
# Test it: Create a book and print its description.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_discription(self):
        print(f"The book {self.title} by {self.author} was published in {self.year} ")
    
book = Book("1999","piyush",2010)
book.get_discription()
 
        