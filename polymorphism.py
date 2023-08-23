#parent class
class Book:
    title = 'unknown'
    author = 'unknown'
    number_of_pages = 0
    book_format = 'Print'

    def book_info(self):
        msg = "\nTitle: {},\nAuthor: {},\nNumber of Pages: {},\nBook Format: {}".format(self.title,self.author,self.number_of_pages,self.book_format)
        return msg

    
#child class
class Horror(Book):
    title = 'From Below'
    author = 'Darcy Coates'
    number_of_pages = 465
    publisher = 'Poisoned Pen Press' #added these attributes that were not part of the parent class
    book_type = 'Paperback'

    def book_info(self):
    #modifying this function to include the addition information added to this child class, demonstrated polymorphism  
        msg = "\nTitle: {},\nAuthor: {},\nNumber of Pages: {},\nBook Format: {}, \nPublisher: {},\nBook Type: {}".format(self.title,self.author,self.number_of_pages,self.book_format,self.publisher,self.book_type)
        return msg
    


#child class
class Classic(Book):
    title = 'Journey to the Center of the Earth'
    author = 'Jules Verne'
    number_of_pages = 146
    year_published = 1864 #added these attributes that were not part of the parent class
    subgenre = 'Fiction'
    
    def book_info(self):
    #modifying this function to include the addition information added to this child class, demonstrated polymorphism 
        msg = "\nTitle: {},\nAuthor: {},\nNumber of Pages: {},\nBook Format: {},\nYear Published: {},\nSubgenre: {}".format(self.title,self.author,self.number_of_pages,self.book_format, self.year_published,self.subgenre)
        return msg


if __name__ == "__main__":
    horror = Horror()
    print(horror.book_info())
    classic = Classic()
    print(classic.book_info())
