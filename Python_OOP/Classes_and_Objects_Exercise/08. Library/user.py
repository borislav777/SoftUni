class User:

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            if self.username not in library.rented_books:
                library.rented_books[self.username] = {book_name: days_to_return}
            else:
                library.rented_books[self.username].update({book_name: days_to_return})
            library.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for username, data in library.rented_books.items():
            for book, days in data.items():
                if book == book_name:
                    return f"The book \"{book_name}\" is already rented and will be available in {days} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name in self.books:
            library.books_available[author].append(book_name)
            library.rented_books[self.username].pop(book_name)
            self.books.remove(book_name)
        return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
