# library_management.py

class Book:
    def __init__(self, title: str, author: str):
        self.title = title               # public
        self.author = author             # public
        self._is_checked_out = False     # "private" by convention

    def check_out(self) -> bool:
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self) -> bool:
        """Mark the book as available if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self) -> bool:
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private collection of Book instances

    def add_book(self, book: Book) -> None:
        """Add a Book to the library."""
        self._books.append(book)

    def _find_book_by_title(self, title: str, *, available: bool | None = None):
        """
        Helper: find the first book by title.
        If available is True, only consider available books.
        If available is False, only consider checked-out books.
        If available is None, ignore availability.
        """
        # Exact title match to align with provided main.py usage.
        for book in self._books:
            if book.title == title:
                if available is None:
                    return book
                if available and book.is_available():
                    return book
                if available is False and not book.is_available():
                    return book
        return None

    def check_out_book(self, title: str) -> bool:
        """
        Check out the first available copy with this title.
        Returns True on success, False if not found or already checked out.
        """
        book = self._find_book_by_title(title, available=True)
        if book:
            return book.check_out()
        return False

    def return_book(self, title: str) -> bool:
        """
        Return the first checked-out copy with this title.
        Returns True on success, False if not found or not checked out.
        """
        book = self._find_book_by_title(title, available=False)
        if book:
            return book.return_book()
        return False

    def list_available_books(self) -> None:
        """
        Print each available book on its own line as:
        Title by Author
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
