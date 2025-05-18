
class Book:
    title: str
    author: str
    year: int
    is_avaible : bool

    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        if not isinstance(year, int):
            raise ValueError("Год публикации должен быть целым числом")
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
    def __len__(self):
        return len(self.books)
    def show_available_books(self):
        print(*self.books,sep="\n\n")

    def add_book(self,book):
        self.books.append(book)

    def borrow_book_by_title(self,title):
        for i in self.books:
            if i.title.lower() == title.lower() :
                if i.is_avaible:
                    print(f"Вы получили книгу: {i.title}")
                    i.is_avaible = False
                else:
                    print(f"Книга: {i.title} уже выдана")
                return
        print(f"У нас нет книги: {i.title}")

    def return_book_by_title(self,title):
        for i in self.books:
            if i.title.lower() == title.lower() :
                if i.is_avaible:
                    print(f"Эта книга уже у нас {i.title}")
                else:
                    print(f"Вы вернули книгу: {i.title}")
                    i.is_avaible = True
                return
        print(f"У нас никогда не было книги : {i.title}")

    def find_books_by_author(self,author):
        total = 0
        for i in self.books:
            if i.author.lower() == author.lower():
                total+=1
                print(i)
            if total==0:
                print(f"У нас книг от : {author}")

    def clear (self):
        self.books = []

def show_menu():
    l= input("Выберите дейсвие:\n"
             "1. Добавить книгу\n"
             "2. Показать доступные книги\n"
             "3. Взять книгу\n"
             "4. Вернуть книгу\n"
             "5. Найти книги по автору\n"
             "6. Очистить библиотеку\n"
             "0. Выход\n"
             "Ваш выбор: ")
    return l


def add_b():
        a= input("Какую книгу вы хотите добавить?:\n"
                 "1. Обычную книгу\n"
                 "2. Художественная книжка\n"
                 "3. Научная книга\n"
                 "Ваш выбор: ")
        b= input("Название книги: ")
        c=input("Автор книги: ")
        d =input("Год публикации книги: ")
        if a =="2":
            f = input("Жанр книги: ")
            book =FictionBook(b,c,d,f)
        elif a=="3":
            f = input("Научная дисциплина или Жанр публикации: ")
            book = ScienceBook(b, c, d, f)
        else:
            book = Book(b,c,d)
        return book



def handle_user_input(library,t):
    if t =="1" or ("доб" in t.lower()):
        library.add_book(add_b())
        with open(r"C:\Users\taras\OneDrive\Документы\Книги.txt","a",encoding="utf-8") as file:
            file.write(str(library.books[-1])+"\n")
        print()
    elif t =="2" or ("показ" in t.lower()):
        library.show_available_books()
        print()
    elif t =="3" or ("взят" in t.lower()):
        a= input("Введите название книги которую хотите взять: ")
        library.borrow_book_by_title(a)
        with open(r"C:\Users\taras\OneDrive\Документы\Книги.txt", "r+", encoding="utf-8") as file:
            new = [line.replace("True","False") if a in line else line for line in file]
            file.seek(0)
            file.writelines(new)
            file.truncate()
    elif t=="4" or ("верну" in t.lower()):
        a = input("Введите название книги которую хотите вернуть: ")
        library.return_book_by_title(a)
        with open(r"C:\Users\taras\OneDrive\Документы\Книги.txt", "r+", encoding="utf-8") as file:
            new = [line.replace("False","True") if a in line else line for line in file]
            file.seek(0)
            file.writelines(new)
            file.truncate()
        print()
    elif t=="5" or ("най" in t.lower()):
        a= input("Введите автора: ")
        library.find_books_by_author(a)
        print()
    elif t=="6" or ("очистка" in t.lower()):
        a=input("Вы уверены что хотите очистить библиотеку((?: ")
        if "д" in a.lower():
            library.clear()
            with open(r"C:\Users\taras\OneDrive\Документы\Книги.txt", "w", encoding="utf-8"):
                pass
            print("Библиотека пуста...")
    else:
        return print("Выберите вариант из списка -_-")


def parsing (line:str):
    line=line.rstrip().split(", ")
    itog ={}
    for i in line:
        key,value = i.split(": ")
        itog[key.lower()] = value
    is_avaible = itog["avaible"] == "True"
    title = itog.get("title","")
    author = itog.get("author","")
    year = itog.get("year",0)
    if "genre" in itog:
        book = FictionBook(title,author,year,itog["genre"])
    elif "field" in itog:
        book = ScienceBook(title,author,year,itog["field"])
    else:
        book = Book(title,author,year)
    book.is_avaible = is_avaible
    return book







def main():
    libray = Library()
    with open(r"C:\Users\taras\OneDrive\Документы\Книги.txt", "r", encoding="utf-8") as file:
        for i in file:
            book = parsing(i)
            libray.add_book(book)
    while True:
        y= show_menu()
        if y=="0" :
            print("Вот что в вашей библиотеке:")
            print(libray.show_available_books())
            break
        handle_user_input(libray,y)



main()


