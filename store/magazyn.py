import random

class DataSet:
    def __init__(self, filename, header, sep=','):
        self.filename = filename
        self.header = header
        self.sep = sep

    def read_file(self):
        header_list = []
        try:
            with open(self.filename, mode='r') as file:
                lines = file.readlines()
                if self.header:
                    header_list.append(lines[0].replace('\n', ''))
                    print('naglowki')
                    return header_list
                print('naglowki')
            return header_list
        except (FileNotFoundError, IOError):
            return "Brak pliku"

    def label(self):
        if  self.header==False:
            return 'Brak etykiet'
        return self.read_file()[0]

    def show_data(self, *args):
        if len(args) == 2:
            var0 = args[0]
            var1 = args[1]


            with open(self.filename, mode='r') as file:
                lines = file.readlines()[var0:var1]
                for el in lines:
                    print(el)
        if len(args) == 0:
            file = self.filename
            with open(file, mode='r') as file:
                lines = file.readlines()
                for el in lines:
                    print(el)

    def training(self, tr=10, t=70, w=20):


        with open(self.filename, mode='r') as file:
            lines = file.readlines()
            random_items = random.choices(lines, k=len(lines))
            tr = round(len(random_items) * tr / 100)
            t = round(len(random_items) * t / 100)
            w = round(len(random_items) * w / 100)

            list_train = [el.replace('\n', '') for el in random_items[:tr]]
            list_test = [el.replace('\n', '') for el in random_items[tr:t]]
            list_valid = [el.replace('\n', '') for el in random_items[t:]]
            return list_train, list_test, list_valid

    def name_decide_clas(self):

        name_of_clas = set()
        with open(self.filename, mode='r') as file:
            lines = file.readlines()
            for line in lines:
                name_of_clas.add(line.split(self.sep)[-1].replace('\n', ''))
        return name_of_clas

    def count_decide_clas(self ):
        name_of_clas = list(self.name_decide_clas())
        decide_clas_dict = {}
        for el in name_of_clas:
            decide_clas_dict[el] = 0

        with open(self.filename, mode='r') as file:
            lines = file.readlines()
            for line in lines:
                for i in range(len(name_of_clas)):
                    if name_of_clas[i] == line.split(self.sep)[-1].replace('\n', ''):
                        decide_clas_dict[name_of_clas[i]] += 1
            return list(decide_clas_dict.items())

    def row_for_decide_clas(self, value_clas):
        list_row = []

        with open(self.filename, mode='r') as file:
            lines = file.readlines()
            for line in lines:
                if value_clas == line.split(self.sep)[-1].replace('\n', ''):
                    list_row.append(line[:-2])
            return list_row

    def inside_dataset(self,  filewrite, list_part=[]):
        with open(self.filename, mode='r') as file:
            lines = file.readlines()
            no_line = int(input('Podaj nr końcowego wiersza '))
            part_dataset = lines[:no_line]
            for row in part_dataset:
                list_part.append(row[:-2])
        with open(filewrite, mode='w') as file:
            for row in list_part:
                file.write(row + '\n')
        return list_part




