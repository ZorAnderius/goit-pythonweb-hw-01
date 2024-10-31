import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    format="%(asctime)s = %(name)s - %(levelname)s: %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("task2.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("Task2")


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Tile: '{self.title}', Author: '{self.author}', Year: '{self.year}'"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f'Book "{book.title}" added successful!')

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info(f'Book "{book.title}" removed successful!')
                break
        else:
            logger.info(f'Book "{title}" not found')

    def show_books(self) -> None:
        if self.books:
            [logger.info(book) for book in self.books]
        else:
            logger.info('Library is empty.')


class LibraryManager:
    def __init__(self, library: Library) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main():
    library: Library = Library()
    manager: LibraryManager = LibraryManager(library)
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
