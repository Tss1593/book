class Book:
    title: str
    author: str
    year: int
    is_avaible : bool

    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.is_avaible= True

    def display_info(self,dop_info=""):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Avaible: {self.is_avaible}{dop_info}")

    def borrow(self):
        if self.is_avaible:
            self.is_avaible = False
            print(f"Вы взяли книгу: {self.title}")
        else:
            print(f"Книга {self.title} уже выдана")

    def return_book(self):
        if self.is_avaible:
            print(f"У вас нет {self.title}")
        else:
            self.is_avaible = True
            print(f"Вы вернули {self.title}")

class FictionBook(Book):
    def __init__(self,title,author,year,genre):
        super().__init__(title,author,year)
        self.genre = genre

    def display_info(self,dop_info=""):
        super().display_info(f", Genre: {self.genre}")

class ScienceBook(Book):
    def __init__(self,title,author,year,field):
        super().__init__(title,author,year)
        self.field = field

    def display_info(self,dop_info=""):
        super().display_info(f", Field: {self.field}")




a= FictionBook("sigmo","Kykold",1488,"droc")
a.display_info()
b= ScienceBook("anal","Niponovick",228,"Sexsologia")
b.display_info()
c=Book("BABY","Sigmo Sigmovick",2005)
c.display_info()
b.borrow()
b.return_book()