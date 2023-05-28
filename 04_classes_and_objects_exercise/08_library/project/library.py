from typing import List, Dict

from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []  # an empty list that will store the users (users objects) of the library
        self.books_available: Dict[str:List[str]] = dict()  # an empty dictionary that will keep information regarding
        # the authors (key: str) and the books available for each of the authors (list of strings)
        self.rented_books: Dict[str:Dict[str:int]] = dict()  # an empty dictionary that will keep information regarding
        # the usernames (key: str) and nested dictionary as a value in which will keep information
        # regarding the book names (key: str) and days left before returning the book to the library
        # (int) - ({usernames: {book names: days to return}})

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        try:
            book = next(
                filter(lambda x: x == book_name, self.books_available[author]))  # finding if the book is available
        except StopIteration:
            return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days!'  # !!!!!!!!!!!!!!!!!!!!!!!!!
        self.books_available[author].remove(book_name)  # removing the book from available list
        if user.username not in self.rented_books.keys():
            self.rented_books[user.username] = dict()
        self.rented_books[user.username][book_name] = days_to_return  # add the book to the rented book list
        user.books.append(book)  # if it is available -> adding to user book list
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User) -> str or None:
        try:
            book_name_for_return = next(filter(lambda x: x == book_name, user.books))
        except StopIteration:
            return f"{user.username} doesn't have this book in his/her records!"
        del self.rented_books[user.username][book_name_for_return] # deleting the book from rented book list
        self.books_available[author].append(book_name) # adding the book again to the available book list
        user.books.remove(book_name) # deleting the book from user book list

