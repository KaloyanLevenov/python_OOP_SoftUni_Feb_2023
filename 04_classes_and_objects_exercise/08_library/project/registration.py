from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library) -> str or None:
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> str or None:
        if user not in library.user_records:
            return "We could not find such user to remove!"
        else:
            library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user_as_object = next(filter(lambda x: x.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"
        if user_as_object.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        old_name = user_as_object.username
        user_as_object.username = new_username
        if old_name in library.rented_books.keys(): # if the user has list with rented books
            library.rented_books[new_username] = library.rented_books[old_name] # creating the same list with his new name
            del library.rented_books[old_name]  # and deleting the list with the old name
        return f"Username successfully changed to: {new_username} for user id: {user_id}"


