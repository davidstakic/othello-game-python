class Racunar(object):
    def __init__(self, boja):
        self.broj_figura = 2
        self.moguci_potezi = []
        self.plocice_za_okretanje = []
        self.boja = boja
    
    def izracunaj_moguce_poteze(self, tabla):
         self.moguci_potezi = []
         smerovi = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
         protivnik = "⚫️" if self.boja == "⚪️" else "⚪️"
         for i in range(8):
             for j in range(8):
                 if tabla.tabla[i][j] == self.boja:
                     for smer in smerovi:
                        x = i + smer[0]
                        y = j + smer[1]
                        if x > 7 or x < 0 or y > 7 or y < 0:
                            continue
                        elif tabla.tabla[x][y] == self.boja or tabla.tabla[x][y] == " ":
                            continue
                        elif tabla.tabla[x][y] == protivnik:
                            x += smer[0]
                            y += smer[1]
                            while x >= 0 and x <= 7 and y >= 0 and y <= 7:
                                if tabla.tabla[x][y] == " ":
                                    if (x, y) not in self.moguci_potezi:
                                        self.moguci_potezi.append((x, y))
                                    break
                                elif tabla.tabla[x][y] == protivnik:
                                    x += smer[0]
                                    y += smer[1]
                                    continue
                                elif tabla.tabla[x][y] == self.boja:
                                    break

    def izracunaj_plocice_za_okretanje(self, tabla, potez):
        self.plocice_za_okretanje = []
        plocice_za_okretanje_jedan_smer = []
        x = potez[0]
        y = potez[1]
        smerovi = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
        protivnik = "⚫️" if self.boja == "⚪️" else "⚪️"
        for smer in smerovi:
            novo_x = x + smer[0]
            novo_y = y + smer[1]
            if novo_x < 0 or novo_x > 7 or novo_y < 0 or novo_y > 7:
                continue
            elif tabla.tabla[novo_x][novo_y] == self.boja:
                continue
            elif tabla.tabla[novo_x][novo_y] == protivnik:
                plocice_za_okretanje_jedan_smer.append((novo_x, novo_y))
                novo_x += smer[0]
                novo_y += smer[1]
                while novo_x >= 0 and novo_x <= 7 and novo_y >= 0 and novo_y <= 7:
                    if tabla.tabla[novo_x][novo_y] == " ":
                        break
                    elif tabla.tabla[novo_x][novo_y] == self.boja:
                        self.plocice_za_okretanje.extend(plocice_za_okretanje_jedan_smer)
                        break
                    elif tabla.tabla[novo_x][novo_y] == protivnik:
                        plocice_za_okretanje_jedan_smer.append((novo_x, novo_y))
                        novo_x += smer[0]
                        novo_y += smer[1]
                        continue
                plocice_za_okretanje_jedan_smer = []

    def okreni_plocice(self, tabla, protivnik):
        for plocica in self.plocice_za_okretanje:
            tabla.tabla[plocica[0]][plocica[1]] = self.boja
            self.broj_figura += 1
            protivnik.broj_figura -= 1
        if self.boja == "⚪️": 
            tabla.broj_belih = self.broj_figura
            tabla.broj_crnih = protivnik.broj_figura
        else:
            tabla.broj_crnih = self.broj_figura
            tabla.broj_belih = protivnik.broj_figura
    
    def moguci_potezi_string(self, tabla):
        tabla.string_za_ispis = ""
    
    def odigraj_potez(self, tabla, potez, protivnik):
        self.izracunaj_moguce_poteze(tabla)
        if potez not in self.moguci_potezi:
            raise Exception("Ne možete odigrati ovaj potez!")
        else:
            tabla.tabla[potez[0]][potez[1]] = self.boja
            self.broj_figura += 1
            if self.boja == "⚪️": 
                tabla.broj_belih = self.broj_figura
            else:
                tabla.broj_crnih = self.broj_figura
            self.izracunaj_plocice_za_okretanje(tabla, potez)
            self.okreni_plocice(tabla, protivnik)
