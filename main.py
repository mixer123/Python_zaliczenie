# Wczytanie datasetu – funkcja, która po podaniu ścieżki (nazwa pliku, jeżeli w tym samym folderze) wczyta
# dane z pliku do listy (można użyć modułu csv). Dodatkowo funkcja przyjmuje parametr określający czy
# pierwszy wiersz pliku zawiera etykiety kolumn czy nie. Jeżeli tak to etykiety wczytywane są do oddzielnej
# listy.
import os
import random


def read_file(filename, header = True):
    header_list = []
    with open(filename, mode ='r') as file:
        lines = file.readlines()

        if header:
            header_list.append(lines[0].replace('\n',''))
            return header_list,filename
    return header_list, filename

# Wypisanie etykiet – funkcja wypisująca etykiety lub komunikat, że etykiet nie było w danym datasecie
def label(file):
    if len(read_file(file, False)[0]) == 0:
        return 'Brak etykiet'
    return [lab for lab in read_file(file)[0].split(',')]

# Wypisanie danych datasetu – funkcja wypisuje kolejne wiersze datasetu. Bez podania parametrów
# wypisywany jest cały dataset, ale możliwe też podanie 2 parametrów, które określają przedział, który ma
# zostać wyświetlony (na wzór slice)

def show_data(*args):
    if len(args)==2:
        var1 = args[0]
        var2 = args[1]

        with open(read_file('iris.csv'), mode='r') as file:
            lines = file.readlines()[var1:var2]
            for el in lines:
                print(el)
    if len(args) == 1:
        file = args[0]
        with open(file, mode='r') as file:
            lines = file.readlines()
            for el in lines:
                print(el)

# Podział datasetu na zbiór treningowy, testowy i walidacyjny. Funkcja przyjmuje 3 parametry określające
# procentowo jaka część głównego zbioru danych trafia do poszczególnych zbiorów

def training(tr=15,t=80,w=5):
    while tr + t + w != 100:
        tr = int(input('Podaj % treningowy='))
        t = int(input('Podaj % testowy='))
        w = int(input('Podaj % walidacyjny='))


    file = read_file('iris.csv', True )[1]
    with open(file, mode='r') as file:
        lines = file.readlines()
        random_items = random.choices(lines, k=len(lines))
        tr = round(len(random_items) * tr / 100)
        t = round(len(random_items) * t / 100)
        w = round(len(random_items) * w / 100)

        list_train = random_items[tr]
        list_test = random_items[tr:t]
        list_valid = random_items[t:]
        return list_train, list_test, list_valid

training(1,2,1)
# print(read_file('iris.csv',True)[1])
# show_data('iris.csv')


# print(label(read_file('iris.csv',True)[1]))
#
