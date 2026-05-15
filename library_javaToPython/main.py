from book import Book
from dvd import DVD

book1 = Book("The Hobbit", "B101", "J.R.R. Tolkien")
dvd1 = DVD("Inception", "D202", 148)

print("Book Information:")
print(book1)
print()

print("DVD Information:")
print(dvd1)
print()

if book1.check_out():
    print(book1.get_title() + " has been checked out.")
else:
    print(book1.get_title() + " is already checked out.")

if book1.check_out():
    print(book1.get_title() + " has been checked out.")
else:
    print(book1.get_title() + " is already checked out.")

if book1.return_item():
    print(book1.get_title() + " has been returned.")
else:
    print(book1.get_title() + " was not checked out.")

print()

if dvd1.check_out():
    print(dvd1.get_title() + " has been checked out.")
else:
    print(dvd1.get_title() + " is already checked out.")

print()
print("Updated DVD Information:")
print(dvd1)
