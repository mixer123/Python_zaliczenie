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
    return header_list

# Wypisanie etykiet – funkcja wypisująca etykiety lub komunikat, że etykiet nie było w danym datasecie
def label(file):
    if len(read_file(file, False)) == 0:
        return 'Brak etykiet'
    return [lab for lab in read_file(file)[0].split(',')]

# Wypisanie danych datasetu – funkcja wypisuje kolejne wiersze datasetu. Bez podania parametrów
# wypisywany jest cały dataset, ale możliwe też podanie 2 parametrów, które określają przedział, który ma
# zostać wyświetlony (na wzór slice)

def show_data(*args):
    pass
print(label('iris.csv'))

read_file('iris.csv')