import random

from store.magazyn import DataSet

'''Menu programu'''
#
dataset = DataSet('iris.csv', True, ',')
while True:
    print('w - wczytaj plik')
    print('l - wypisanie etykiet')
    print('s - Wypisanie danych datasetu')
    print('p - Podział datasetu')
    print('r - Wypisz liczbę klas decyzyjnych ')
    print('m - Wypisz dane dla podanej wartości klasy decyzyjnej ')
    print('x -  Zapisanie  danych do pliku csv')
    print('q - exit')

    key = input('Podaj klucz z klawiatury:  ')
    if key == 'w':
        print(dataset.read_file())
    if key == 'l':
        print(dataset.label())
    if key == 's':
        print(dataset.show_data())
    if key == 'p':
        dataset.training()
    if key == 'r':
        print(dataset.count_decide_clas())
    if key == 'm':
        print(dataset.row_for_decide_clas('Iris-virginica'))
    if key == 'x':
        dataset.inside_dataset('write.csv')
    if key == 'q':
        break





# print(dataset.read_file())
# print(dataset.label())
# # dataset.show_data()
# # print(dataset.training()[0])
# # print(dataset.count_decide_clas())
# print(dataset.row_for_decide_clas('Iris-virginica'))
# dataset.inside_dataset('write.csv')
