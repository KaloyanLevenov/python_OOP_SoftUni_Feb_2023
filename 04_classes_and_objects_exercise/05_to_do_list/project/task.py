from typing import List


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed: bool = False

    def change_name(self, new_name: str) -> str or None:
        if new_name == self.name:
            return "Name cannot be the same."
        else:
            self.name = new_name
            return new_name

    def change_due_date(self, new_date: str) -> str or None:
        if new_date == self.due_date:
            return "Date cannot be the same."
        else:
            self.due_date = new_date
            return new_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        else:
            return "Cannot find comment."

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"


