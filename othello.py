import igrac
import racunar
import tabla
import heuristika
from time import sleep
from copy import deepcopy

class Othello(object):
    def __init__(self, boja_igrac, boja_cpu):
        self.tabla = tabla.Tabla()
        self.igrac = igrac.Igrac(boja_igrac)
        self.cpu = racunar.Racunar(boja_cpu)
        self.heuristika = heuristika.Heuristika()
        self.izracunata_stanja = {}

    def stanje_table_igrac(self):
        self.igrac.moguci_potezi_string(self.tabla)
        tabla_za_ispis = deepcopy(self.tabla.tabla)
        for potez in self.igrac.moguci_potezi:
            tabla_za_ispis[potez[0]][potez[1]] = "💢"
        self.tabla.ispisi_tablu(tabla_za_ispis)

    def stanje_table_cpu(self):
        self.cpu.moguci_potezi_string(self.tabla)
        self.tabla.ispisi_tablu(self.tabla.tabla)

    def kraj_igre(self):
        if (self.tabla.broj_belih + self.tabla.broj_crnih == 64) or (self.tabla.broj_belih == 0) or (self.tabla.broj_crnih == 0) or (len(self.igrac.moguci_potezi) == 0 and len(self.cpu.moguci_potezi) == 0):
            return True
        return False

    def odredi_pobednika(self):
        self.stanje_table_cpu()
        if self.tabla.broj_belih > self.tabla.broj_crnih:
            print("Beli je pobedio!")
            sleep(5)
        elif self.tabla.broj_belih < self.tabla.broj_crnih:
            print("Crni je pobedio!")
            sleep(5)
        else:
            print("Nerešeno je!")
            sleep(5)
        
    def minimax(self, tabla, depth, alpha, beta, maximizing_player, cpu, igrac):
        stanje = self.tabla.tabla_string(tabla.tabla)
        if stanje in self.izracunata_stanja:
            return self.izracunata_stanja[stanje]
        if depth == 0 or self.kraj_igre():
            rezultat = self.heuristika.heuristika(tabla, cpu, igrac)
            self.izracunata_stanja[stanje] = rezultat
            return rezultat
        if maximizing_player:
            maxEval = float('-inf')
            cpu.izracunaj_moguce_poteze(tabla)
            for potez in cpu.moguci_potezi:
                kopija_table = deepcopy(tabla)
                cpu.odigraj_potez(kopija_table, potez, igrac)
                rezultat = self.minimax(kopija_table, depth - 1, alpha, beta, False, cpu, igrac)
                maxEval = max(maxEval, rezultat)
                alpha = max(alpha, rezultat)
                if beta <= alpha:
                    break
            self.izracunata_stanja[stanje] = maxEval
            return maxEval
        else:
            minEval = float('inf')
            igrac.izracunaj_moguce_poteze(tabla)
            for potez in igrac.moguci_potezi:
                kopija_table = deepcopy(tabla)
                string_potez = igrac.pozicija_string(potez)
                igrac.odigraj_potez(kopija_table, string_potez, cpu)
                rezultat = self.minimax(kopija_table, depth - 1, alpha, beta, True, cpu, igrac)
                minEval = min(minEval, rezultat)
                beta = min(beta, rezultat)
                if beta <= alpha:
                    break
            self.izracunata_stanja[stanje] = minEval
            return minEval
    
    def igraj(self, izbor):
        dubina = 6
        if izbor == "CRNI":
            self.igrac.izracunaj_moguce_poteze(self.tabla)
            self.cpu.izracunaj_moguce_poteze(self.tabla)
            while not self.kraj_igre():
                self.stanje_table_igrac()
                if len(self.igrac.moguci_potezi) != 0:
                    print("Vi ste na redu!\n")
                    while True:
                        try:
                            potez = input("Odigrajte potez: ").upper().strip()
                            self.igrac.odigraj_potez(self.tabla, potez, self.cpu)
                            break
                        except Exception as e:
                            print(e)
                    if self.kraj_igre():
                        break
                else:
                    sleep(1)
                
                self.stanje_table_cpu()
                self.cpu.izracunaj_moguce_poteze(self.tabla)
                if len(self.cpu.moguci_potezi) == 0:
                    print("Trenutno ne postoji potez koji računar može da odigra. Preskače se njegov red.")
                    sleep(1)
                else:
                    if len(self.cpu.moguci_potezi) == 1:
                        dubina = 7
                    elif len(self.cpu.moguci_potezi) > 1 and len(self.cpu.moguci_potezi) <= 4:
                        dubina = 6
                    elif len(self.cpu.moguci_potezi) > 4 and len(self.cpu.moguci_potezi) <= 8:
                        dubina = 5
                    else:
                        dubina = 4
                    print("Računar odigrava potez...")
                    najbolji_rezultat = float('-inf')
                    najbolji_potez = None
                    for potez in self.cpu.moguci_potezi:
                        kopija_igrac = deepcopy(self.igrac)
                        kopija_cpu = deepcopy(self.cpu)
                        kopija_table = deepcopy(self.tabla)
                        kopija_cpu.odigraj_potez(kopija_table, potez, kopija_igrac)
                        rezultat = self.minimax(kopija_table, dubina, float('-inf'), float('inf'), False, kopija_cpu, kopija_igrac)
                        if rezultat >= najbolji_rezultat:
                            najbolji_rezultat = rezultat
                            najbolji_potez = potez
                    self.cpu.odigraj_potez(self.tabla, najbolji_potez, self.igrac)
        else:
            self.igrac.izracunaj_moguce_poteze(self.tabla)
            self.cpu.izracunaj_moguce_poteze(self.tabla)
            while not self.kraj_igre():
                self.stanje_table_cpu()
                self.cpu.izracunaj_moguce_poteze(self.tabla)
                if len(self.cpu.moguci_potezi) == 0:
                    print("Trenutno ne postoji potez koji računar može da odigra. Preskače se njegov red.")
                    sleep(1)
                else:
                    if len(self.cpu.moguci_potezi) == 1:
                        dubina = 7
                    elif len(self.cpu.moguci_potezi) > 1 and len(self.cpu.moguci_potezi) <= 4:
                        dubina = 6
                    elif len(self.cpu.moguci_potezi) > 4 and len(self.cpu.moguci_potezi) <= 8:
                        dubina = 5
                    else:
                        dubina = 4
                    print("Računar odigrava potez...")
                    najbolji_rezultat = float('-inf')
                    najbolji_potez = None
                    for potez in self.cpu.moguci_potezi:
                        kopija_igrac = deepcopy(self.igrac)
                        kopija_cpu = deepcopy(self.cpu)
                        kopija_table = deepcopy(self.tabla)
                        kopija_cpu.odigraj_potez(kopija_table, potez, kopija_igrac)
                        rezultat = self.minimax(kopija_table, dubina, float('-inf'), float('inf'), False, kopija_cpu, kopija_igrac)
                        if rezultat >= najbolji_rezultat:
                            najbolji_rezultat = rezultat
                            najbolji_potez = potez
                    self.cpu.odigraj_potez(self.tabla, najbolji_potez, self.igrac)
                    if self.kraj_igre():
                        break

                self.stanje_table_igrac()
                if len(self.igrac.moguci_potezi) != 0:
                    print("Vi ste na redu!\n")
                    while True:
                        try:
                            potez = input("Odigrajte potez: ").upper().strip()
                            self.igrac.odigraj_potez(self.tabla, potez, self.cpu)
                            break
                        except Exception as e:
                            print(e)
                else:
                    sleep(1)

        self.odredi_pobednika()

