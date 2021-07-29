class PhotoAlbum:
    PAGE_PHOTOS = 4
    DASHES = 11

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
        self.index = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // cls.PAGE_PHOTOS
        return cls(pages)

    def add_photo(self, label):
        if self.pages > self.index and len(self.photos[self.index]) < PhotoAlbum.PAGE_PHOTOS:
            self.photos[self.index].append(label)

            result = f"{label} photo added successfully on page {self.index + 1} slot {len(self.photos[self.index])}"
            if len(self.photos[self.index]) == PhotoAlbum.PAGE_PHOTOS:
                self.index += 1
            return result

        return "No more free slots"

    def display(self):
        result = f"{'-' * PhotoAlbum.DASHES}\n"
        for page in self.photos:
            result += f"{' '.join(['[]' for _ in range(len(page))])}\n"
            result += f"{'-' * PhotoAlbum.DASHES}\n"

        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
