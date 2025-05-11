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

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Avaible: {self.is_avaible}"

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

    def __str__(self):
        return super().__str__() + f", Genre: {self.genre}"

    def display_info(self,dop_info=""):
        super().display_info(f", Genre: {self.genre}")


class ScienceBook(Book):
    def __init__(self,title,author,year,field):
        super().__init__(title,author,year)
        self.field = field

    def __str__(self):
        return super().__str__() + f", Field: {self.field}"

    def display_info(self,dop_info=""):
        super().display_info(f", Field: {self.field}")


class Library:
    books : list

    def __init__(self):
        self.books = []

    def show_available_books(self):
        print(*self.books,sep="\n\n")

    def add_book(self,book):
        self.books.append(book)

    def borrow_book_by_title(self,title):
        for i in self.books:
            if i.title == title :
                if i.is_avaible:
                    print(f"Вы получили книгу: {i.title}")
                    i.is_avaible = False
                else:
                    print(f"Книга: {i.title} уже выдана")
            else:
                print(f"У нас нет книги: {i.title}")

    def return_book_by_title(self,title):
        for i in self.books:
            if i.title == title :
                if i.is_avaible:
                    print(f"Эта книга уже у нас {i.title}")
                else:
                    print(f"Вы вернули книгу: {i.title}")
                    i.is_avaible = True
            else:
                print(f"У нас никогда не было книги : {i.title}")

    def find_books_by_author(self,author):
        for i in self.books:
            total = 0
            if i.author == author:
                total+=1
                print(i)
            if total==0:
                print(f"У нас книг от : {author}")



a= FictionBook("sigmo","Kykold",1488,"droc")
b= ScienceBook("anal","Niponovick",228,"Sexsologia")
c=Book("BABY","Sigmo Sigmovick",2005)
g= Library()
g.add_book(a)
g.show_available_books()
g.find_books_by_author("Kaa")
