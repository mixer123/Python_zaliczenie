# Ćwiczenie 2. Stwórz klasę Book z kilkoma z kilkoma polami
# i konstruktorem ustanawiającym pola.
# Spróbuj na różne sposoby dodać metodę __eq__.



class Book:
    def __init__(self, title, author, publisher, year):

       self.title = title
       self.author = author
       self.publisher = publisher
       self.year = year


    def __str__(self):
        return f'{self.title} {self.author}'

    def __repr__(self):
        return f'{self.title} {self.author}'

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author \
            and self.publisher == other.publisher



books1 = Book('tytul1', 'autor1', 'publisher1', 1991)
books2 = Book('tytul2', 'autor2', 'publisher2', 1992)

print(books1)
print(books2)
print(books1 == books1)
print(books1 is books2)
