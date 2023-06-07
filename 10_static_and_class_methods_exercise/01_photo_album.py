from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_ON_A_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List] = [[] for _ in range(self.pages)]
        # Each page can contain only 4 photos !


    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / cls.PHOTOS_ON_A_PAGE)
        return cls(pages)

    def add_photo(self, label:str) -> str:
        page_number = 0
        for page in self.photos:
            page_number += 1
            if len(page) == self.PHOTOS_ON_A_PAGE:
                continue
            page.append(label)
            slot_number = len(page)
            return f"{label} photo added successfully on page " \
                   f"{page_number} slot {slot_number}"
        else:
            return "No more free slots"

    def display(self) -> str:
        result = ["-" * 11]
        for page in self.photos:
            result.append((''.join('[] ' * len(page))).rstrip())
            result.append("-" * 11)

        return '\n'.join(result)