# Ćwiczenie. Stwórz klasę Book z polami title, author, publisher, year.
# Dodaj w klasie inicjalizator oraz metodę zwracającą napis z reprezentacją obiektu.
#
# Zapewnij następujące kryteria sprawdzające:
#
#     pole author i title są napisami - w przeciwnym wypadku ustaw pusty napis "".
#     rok ma być dodatnią liczbą całkowitą


class Book:
    def __init__(self, title, author, publisher, year):
        if isinstance(title, str):
            self.__title = title
        else:
            self.__title = "default title"

        if isinstance(author, str):
            self.__author = author
        else:
            self.__author = " default author"

        self.publisher = publisher

        if isinstance(year, int) and year >0:
            self.__year = year
        else:
            self.__year = 2000

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, value):
        self.__title = value

    def set_author(self, value):
        self.__author = value


    def __str__(self):
        return f'{self.get_author()} {self.get_title()}'

    def __repr__(self):
        return f'{self.get_author()} {self.get_title()}'



books = Book('tytul1', 'autor1', 'publisher1', 1991),

print(books)
