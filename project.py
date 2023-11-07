import csv
import sys

booklist = []


class Book:
    def __init__(self, bookname, page, notes=None, rating=None):
        self.bookname = bookname
        self.page = page
        self.notes = notes
        self.rating = rating

    def __str__(self):
        return f"Book: {self.bookname}\nPage: {self.page}\nNotes: {self.notes}\nRating: {self.rating}"

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        try:
            if rating:
                if rating.isnumeric():
                    if int(rating) >= 1 and int(rating) <= 10:
                        self._rating = int(rating)
                    else:
                        print("Rating must be an integer between 1 and 10, inclusive.")
                else:
                    print("Rating must be an integer between 1 and 10, inclusive.")
            else:
                self._rating = None
        except ValueError:
            print("Rating must be an integer between 1 and 10, inclusive.")

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page):
        try:
            if int(page) >= 0:
                self._page = int(page)
            else:
                print("Page cannot be negative.")
        except:
            print("Page must be a number.")


def main():
    csv_reader()
    while True:
        print("WELCOME TO BOOK TRACKER!!! :)")
        print('      Enter "1" to view books, page numbers, notes, and ratings')
        print('      Enter "2" to add a book')
        print('      Enter "3" to delete a book')
        print('      Enter "4" to change the page number of a book')
        print('      Enter "5" to add notes')
        print('      Enter "6" to rate a book')
        print('      Enter "7" to exit the program\n')
        number = input()
        if menu_number_validator(number):
            function_caller(int(number))
        else:
            print("Please enter a number between 1 and 7 :)")


def csv_reader():
    global booklist
    try:
        with open("books.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                booklist.append(Book(row[0], row[1], row[2], row[3]))
    except:
        with open("books.csv", "w") as file:
            pass


def csv_updater():
    with open("books.csv", "w") as file:
        writer = csv.writer(file)
        for book in booklist:
            writer.writerow([book.bookname, book.page, book.notes, book.rating])

def menu_number_validator(menu_number):
    if menu_number.isnumeric():
        menu_number = int(menu_number)
        if menu_number == 7:
                sys.exit("Thank you for using BOOK TRACKER! Keep reading :)")
        elif menu_number >=1 and menu_number <=6:
            return True
        else:
            return False
    else:
        return False

def book_number_validator(booknumber):
    if booknumber.isnumeric():
        if int(booknumber) >= 1 and int(booknumber) <= len(booklist):
            return True
        else:
            return False
    else:
        return False


def function_caller(number):
    print()
    if number == 1:
        print(view_books())
    elif number == 2:
        add_book()
    elif number == 3:
        delete_book()
    elif number == 4:
        change_page()
    elif number == 5:
        add_notes()
    else:
        rate_book()


def view_books():
    if len(booklist) >= 1:
        bookandindex = ""
        for index, book in enumerate(booklist):
            bookandindex+=(f"{index+1}.\n{book}\n")
        return bookandindex
    else:
        return("You have 0 books in book tracker. Feel free add some :)\n")


def add_book():
    global booklist
    bookname = input("What is the book's name? ")
    page = input("What page are you on? ")
    booklist.append(Book(bookname, page))
    csv_updater()


def delete_book():
    global booklist
    view_books()
    if len(booklist) > 0:
        deleteindex = input(
            "Which book do you want to delete? Enter the book number above the book.\n"
        )
        if book_number_validator(deleteindex) == True:
            booklist.pop(int(deleteindex) - 1)
            csv_updater()
        else:
            print("Invalid input. Try again.")


def change_page():
    global booklist
    view_books()
    booknumber = input(
        "Which book's page number do you want to change? Enter the book number above the book.\n"
    )
    if book_number_validator(booknumber) == True:
        bookpage = input("What page are you on?\n")
        booklist[int(booknumber) - 1].page = int(bookpage)
        csv_updater()
    else:
        print("Invalid input. Try again.")


def add_notes():
    view_books()
    booknumber = input(
        "Which book do you want to add notes for? Enter the book number above the book.\n"
    )
    if book_number_validator(booknumber) == True:
        notes = input("Input your notes: ")
        booklist[int(booknumber) - 1].notes = notes
        csv_updater()
    else:
        print("Invalid input. Try again.")


def rate_book():
    global booklist
    view_books()
    booknumber = input(
        "Which book do you want to rate? Enter the book number above the book.\n"
    )
    if book_number_validator(booknumber) == True:
        bookrating = input("Rate this book from 1 to 10, inclusive.\n")
        booklist[int(booknumber) - 1].rating = bookrating
        csv_updater()
    else:
        print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
