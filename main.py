# Wczytanie datasetu – funkcja, która po podaniu ścieżki (nazwa pliku, jeżeli w tym samym folderze) wczyta
# dane z pliku do listy (można użyć modułu csv). Dodatkowo funkcja przyjmuje parametr określający czy
# pierwszy wiersz pliku zawiera etykiety kolumn czy nie. Jeżeli tak to etykiety wczytywane są do oddzielnej
# listy.

import random


def read_file(filename,header = True, sep=','):
    header_list = []
    try:
        with open(filename, mode ='r') as file:
            lines = file.readlines()
            if header:
                header_list.append(lines[0].replace('\n',''))
                return header_list,filename,sep, header
        return header_list, filename, sep, header
    except (FileNotFoundError, IOError):
        return "Brak pliku"



# Wypisanie etykiet – funkcja wypisująca etykiety lub komunikat, że etykiet nie było w danym datasecie
def label(file, header=True):
    if  read_file(file,header,',')[3]==False:
        return 'Brak etykiet'
    # sep = read_file(file)[2]
    return [lab for lab in read_file(file)[0]]

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
    tr = int(input('Podaj tr trening'))
    t = int(input('Podaj t test'))
    w = int(input('Podaj w walidacja'))


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

def name_decide_clas(file,sep):
    file = read_file(file,header = True, sep=sep)[1]
    name_of_clas = set()
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            name_of_clas.add(line.split(sep)[-1].replace('\n',''))
    return name_of_clas
def count_decide_clas(file,sep):
    name_of_clas = list(name_decide_clas(file,sep))
    decide_clas_dict = {}
    for el in name_of_clas:
        decide_clas_dict[el] = 0
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            for i in range(len(name_of_clas)):
                if name_of_clas[i] == line.split(sep)[-1].replace('\n',''):
                    decide_clas_dict[name_of_clas[i]] += 1
        return list(decide_clas_dict.items())


'''Wypisz dane dla podanej wartości klasy decyzyjnej – wypisuje wiersze 
z zadaną wartością klasy decyzyjnej.'''

def row_for_decide_clas(file, sep, value_clas):
    list_row =[]
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            if value_clas == line.split(sep)[-1].replace('\n', ''):
                list_row.append(line[:-2])
        return list_row


'''Zapisanie danych do pliku csv – jako parametr przyjmowana jest dowolna lista, 
która może być podzbiorem datasetu, zmienną przechowującą dane treningowe, itp. 
Dodatkowo podawana jest nazwa pliku, do którego dane zostaną zapisane.'''

def inside_dataset(fileopen,filewrite, list_part=[]):
    with open(fileopen, mode='r') as file:
        lines = file.readlines()
        no_line = int(input('Podaj nr końcowego wiersza '))
        part_dataset = lines[:no_line]
        for row in part_dataset:
            list_part.append(row[:-2])
    with open(filewrite, mode='w') as file:
        for row in list_part:
            file.write(row+'\n')
    return list_part

'''Menu programu'''

while True:
    print('w - wczytaj plik')
    print('l - wypisanie etykiet')
    print('s - Wypisanie danych datasetu')
    print('p - Podział datasetu')
    print('q - exit')

    key = input('Podaj klucz z klawiatury:  ')
    if key == 'w':
        print(read_file('iris.csv', True))
    if key == 'l':
        print(label(read_file('iris.csv')[1]))
    if key == 'l':
        print(show_data('iris.csv'))
    if key == 'p':
        training('iris.csv')
    if key == 'q':
        break



# print(inside_dataset('iris.csv','write.csv'))
# print(name_decide_clas('iris.csv',','))
# print(row_for_decide_clas('iris.csv', ',', 'Iris-setosa'))
# print(count_decide_clas('iris.csv',','))
# training('iris.csv', 1,2,1)
# print(name_decide_clas('iris.csv',','))
# print(training('iris.csv', 15,80,5)[0])
# print(read_file('iris.csv',True))
# show_data('iris.csv')


print(label(read_file('iris.csv',False)[1]))
#
