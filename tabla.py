from tabulate import tabulate
from colorama import Back

class Tabla(object):
    def __init__(self):
        self.tabla = [[" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", "⚪️", "⚫️", " ", " ", " "],
                       [" ", " ", " ", "⚫️", "⚪️", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "]]
        self.broj_belih = 2
        self.broj_crnih = 2
        self.string_za_ispis = ""

    def ispisi_tablu(self, tabla):
        headers = [" ", "A", "B", "C", "D", "E", "F", "G", "H", " "]
        table_data = []
        for i, row in enumerate(tabla):
            row_data = [str(i+1)] + row + [str(i+1)]
            table_data.append(row_data)
        table_data.insert(0, headers)
        table_data.append(headers)
        table_str = tabulate(table_data, tablefmt="simple_grid")
        print("\033c")
        print("Crni: " + str(self.broj_crnih) + " Beli: " + str(self.broj_belih) + "\n")
        print(Back.GREEN + table_str)
        print(Back.RESET + '\n')
        print(self.string_za_ispis)

    def tabla_string(self, tabla):
        string = ""
        for i in range(8):
            for j in range(8):
                string += tabla[i][j]
        return string
