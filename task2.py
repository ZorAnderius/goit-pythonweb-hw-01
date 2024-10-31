from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Tile: '{self.title}', Author: '{self.author}', Year: '{self.year}'"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self):
        [print(book) for book in self.books]


class LibraryManager:
    def __init__(self, library: Library):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)
    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter title book: ").strip()
                author = input("Enter book's author: ").strip()
                year = input("Enter book's year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book's title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
