# Wczytanie datasetu – funkcja, która po podaniu ścieżki (nazwa pliku, jeżeli w tym samym folderze) wczyta
# dane z pliku do listy (można użyć modułu csv). Dodatkowo funkcja przyjmuje parametr określający czy
# pierwszy wiersz pliku zawiera etykiety kolumn czy nie. Jeżeli tak to etykiety wczytywane są do oddzielnej
# listy.

def read_file(file, header=True):
    header_list=[]
    with open(file, mode ='r') as file:
        lines = file.readlines()

        if header:
            header_list.append(lines[0].replace('\n',''))
            return header_list
    return header_list, file

# Wypisanie etykiet – funkcja wypisująca etykiety lub komunikat, że etykiet nie było w danym datasecie
def label(file):
    if len(read_file(file, False)[0]) == 0:
        return 'Brak etykiet'
    return [lab for lab in read_file(file)[0].split(',')]

# Wypisanie danych datasetu – funkcja wypisuje kolejne wiersze datasetu. Bez podania parametrów
# wypisywany jest cały dataset, ale możliwe też podanie 2 parametrów, które określają przedział, który ma
# zostać wyświetlony (na wzór slice)

def show_data(*args):
    if len(args)==3:
        var1 = args[0]
        var2 = args[1]
        file = args[2]
        with open(file, mode='r') as file:
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

def trening(tr,t,w,file):
    pass


# read_file('iris.csv')
show_data('iris.csv')


# print(label('iris.csv'))
#
