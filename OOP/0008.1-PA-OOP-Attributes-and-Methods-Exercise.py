# 01. Photo Album
# from math import ceil
#
#
# class PhotoAlbum:
#     def __init__(self, pages: int):
#         self.pages = pages
#         self.photos = [[] for _ in range(pages)]
#
#     @classmethod
#     def from_photos_count(cls, photos_count: int):
#         return cls(ceil(photos_count / 4))
#
#     def add_photo(self, label: str):
#         for _page in self.photos:
#             if len(_page) < 4:
#                 _page.append(label)
#                 return f"{label} photo added successfully on page {self.photos.index(_page) + 1} slot {_page.index(label) + 1}"
#         return f"No more free spots"
#
#     def display(self):
#         _line = "-" * 11
#         _album = [_line]
#         for _page in self.photos:
#             _album.append(('[] ' * len(_page)).rstrip(' '))
#             _album.append(_line)
#
#         return '\n'.join(_album) + '\n'
#
#
# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
