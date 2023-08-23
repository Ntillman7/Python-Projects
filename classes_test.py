#parent class
class Book:
    def __init__(self, title, author):
       self.title = title 
       self.author = author
    

    def __str__(self):
        return f"\n{self.title} by {self.author}"

    def more_info(self):
        msg = "\nThis book is 418 pages long and is a harcover book."
        print(msg)

class Horror(Book):
    pass

book2 = Book("From Below", "Darcy Coates")
    


if __name__ == "__main__":
    book1 = Book("Dracula", "Bram Stoker")
    print(book1)
    book1.more_info()
    print(book2)
   
 def review(self):
       rating = input("Enter your rating out of 10 here: ")
       if rating <= 10
       print(rating)
       else:
           print('Please choose a score out of 10.')
