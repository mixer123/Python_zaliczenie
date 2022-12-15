# Wczytanie datasetu – funkcja, która po podaniu ścieżki (nazwa pliku, jeżeli w tym samym folderze) wczyta
# dane z pliku do listy (można użyć modułu csv). Dodatkowo funkcja przyjmuje parametr określający czy
# pierwszy wiersz pliku zawiera etykiety kolumn czy nie. Jeżeli tak to etykiety wczytywane są do oddzielnej
# listy.

import random


def read_file(filename,header = True, sep=','):
    header_list = []

    with open(filename, mode ='r') as file:
        lines = file.readlines()

        if header:
            header_list.append(lines[0].replace('\n',''))
            return header_list,filename,sep
    return header_list, filename, sep

# Wypisanie etykiet – funkcja wypisująca etykiety lub komunikat, że etykiet nie było w danym datasecie
def label(file):
    if len(read_file(file, False)[0]) == 0:
        return 'Brak etykiet'
    sep = read_file(file, False)[2]
    return [lab for lab in read_file(file)[0].split(sep)]

# Wypisanie danych datasetu – funkcja wypisuje kolejne wiersze datasetu. Bez podania parametrów
# wypisywany jest cały dataset, ale możliwe też podanie 2 parametrów, które określają przedział, który ma
# zostać wyświetlony (na wzór slice)

def show_data(*args):
    if len(args) == 3:
        var0 = args[0]
        var1 = args[1]
        var2 = args[2]


        with open(var2, mode='r') as file:
            lines = file.readlines()[var0:var1]
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

def training(file, tr=15,t=80,w=5):


    file = read_file(file, True )[1]
    with open(file, mode='r') as file:
        lines = file.readlines()
        random_items = random.choices(lines, k=len(lines))
        tr = round(len(random_items) * tr / 100)
        t = round(len(random_items) * t / 100)
        w = round(len(random_items) * w / 100)

        list_train = [ el.replace('\n','') for el in random_items[:tr] ]
        list_test =  [ el.replace('\n','') for el in random_items[tr:t] ]
        list_valid = [ el.replace('\n','') for el in  random_items[t:] ]
        return list_train, list_test, list_valid



"""Wypisz liczbę klas decyzyjnych – wypisanie krotek gdzie pierwsza wartość 
to wartość klasy (np. nazwa irysa,
dla binarnych 0 lub 1 itd.), a druga to liczebność (kardynalność) tej klasy"""

def decide_clas(file,sep):
    file = read_file(file,header = True, sep=sep)[1]
    name_of_clas = set()
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            name_of_clas.add(line.split(sep)[-1].replace('\n',''))
    return name_of_clas


# training('iris.csv', 1,2,1)
print(decide_clas('iris.csv',','))
# print(training('iris.csv', 15,80,5)[0])
# print(read_file('iris.csv',True)[1])
# show_data('iris.csv')


# print(label(read_file('iris.csv',True)[1]))
#
