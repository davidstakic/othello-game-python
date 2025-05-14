class Heuristika(object):
    def __init__(self):
        pass

    def izracunaj_razliku_u_figurama(self, myPlayer, oppPlayer):
        if myPlayer.broj_figura > oppPlayer.broj_figura:
            return (100.0 * myPlayer.broj_figura) / (myPlayer.broj_figura + oppPlayer.broj_figura)
        elif myPlayer.broj_figura < oppPlayer.broj_figura:
            return (100.0 * oppPlayer.broj_figura) / (myPlayer.broj_figura + oppPlayer.broj_figura)
        return 0
    
    def izracunaj_vrednosti_polja_i_ivicnih(self, tabla, myPlayer, oppPlayer):
        d = 0
        myPlayer_na_ivici = 0
        oppPlayer_na_ivici = 0
        smerovi = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
        vrednosti_za_polja = [[20, -3, 11, 8, 8, 11, -3, 20],
                              [-3, -7, -4, 1, 1, -4, -7, -3],
                              [11, -4, 2, 2, 2, 2, -4, 11],
                              [8, 1, 2, -3, -3, 2, 1, 8],
                              [8, 1, 2, -3, -3, 2, 1, 8],
                              [11, -4, 2, 2, 2, 2, -4, 11],
                              [-3, -7, -4, 1, 1, -4, -7, -3],
                              [20, -3, 11, 8, 8, 11, -3, 20]]
        for i in range(8):
            for j in range(8):
                if tabla.tabla[i][j] == myPlayer.boja:
                    d += vrednosti_za_polja[i][j]
                elif tabla.tabla[i][j] == oppPlayer.boja:
                    d -= vrednosti_za_polja[i][j]
                elif tabla.tabla[i][j] != " ":
                    for smer in smerovi:
                        x = i + smer[0]
                        y = j + smer[1]
                        if x >= 0 and x <= 7 and y >= 0 and y <= 7 and tabla.tabla[x][y] == " ":
                            if tabla.tabla[i][j] == myPlayer.boja:
                                myPlayer_na_ivici += 1
                            else:
                                oppPlayer_na_ivici += 1
                            break
        if myPlayer_na_ivici > oppPlayer_na_ivici:
            f = -(100.0 * myPlayer_na_ivici) / (myPlayer_na_ivici + oppPlayer_na_ivici)
        elif myPlayer_na_ivici < oppPlayer_na_ivici:
            f = (100.0 * oppPlayer_na_ivici) / (myPlayer_na_ivici + oppPlayer_na_ivici)
        else:
            f = 0
        return (d, f)
    
    def izracunaj_zauzetost_coskova(self, tabla, myPlayer, oppPlayer):
        myPlayer_u_cosku = 0
        oppPlayer_u_cosku = 0
        if tabla.tabla[0][0] == myPlayer.boja:
            myPlayer_u_cosku += 1
        elif tabla.tabla[0][0] == oppPlayer.boja:
            oppPlayer_u_cosku += 1
        if tabla.tabla[0][7] == myPlayer.boja:
            myPlayer_u_cosku += 1
        elif tabla.tabla[0][7] == oppPlayer.boja:
            oppPlayer_u_cosku += 1
        if tabla.tabla[7][0] == myPlayer.boja:
            myPlayer_u_cosku += 1
        elif tabla.tabla[7][0] == oppPlayer.boja:
            oppPlayer_u_cosku += 1
        if tabla.tabla[7][7] == myPlayer.boja:
            myPlayer_u_cosku += 1
        elif tabla.tabla[7][7] == oppPlayer.boja:
            oppPlayer_u_cosku += 1
        return 25 * (myPlayer_u_cosku - oppPlayer_u_cosku)
    
    def izracunaj_pozicije_do_coskova(self, tabla, myPlayer, oppPlayer):
        myPlayer_do_coska =  0
        oppPlayer_do_coska = 0
        if tabla.tabla[0][0] == " ":
            if tabla.tabla[0][1] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[0][1] == oppPlayer.boja:
                oppPlayer_do_coska += 1
            if tabla.tabla[1][1] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[1][1] == oppPlayer.boja:
                oppPlayer_do_coska += 1
            if tabla.tabla[1][0] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[1][0] == oppPlayer.boja:
                oppPlayer_do_coska += 1

        if tabla.tabla[0][7] == " ":
            if tabla.tabla[0][6] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[0][6] == oppPlayer.boja:
                oppPlayer_do_coska += 1
            if tabla.tabla[1][6] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[1][6] == oppPlayer.boja:
                oppPlayer_do_coska += 1
            if tabla.tabla[1][7] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[1][7] == oppPlayer.boja:
                oppPlayer_do_coska += 1
        
        if tabla.tabla[7][0] == " ":
            if tabla.tabla[7][1] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[7][1] == oppPlayer.boja:
                oppPlayer_do_coska += 1
            if tabla.tabla[6][1] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[6][1] == oppPlayer.boja:
                oppPlayer_do_coska += 1
            if tabla.tabla[6][0] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[6][0] == oppPlayer.boja:
                oppPlayer_do_coska += 1
        
        if tabla.tabla[7][7] == " ":
            if tabla.tabla[6][7] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[6][7] == oppPlayer.boja:
                oppPlayer_do_coska += 1
            if tabla.tabla[6][6] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[6][6] == oppPlayer.boja:
                oppPlayer_do_coska += 1
            if tabla.tabla[7][6] == myPlayer.boja:
                myPlayer_do_coska += 1
            elif tabla.tabla[7][6] == oppPlayer.boja:
                oppPlayer_do_coska += 1

        return -12.5 * (myPlayer_do_coska - oppPlayer_do_coska)
    
    def mobilnost(self, myPlayer, oppPlayer):
        myPlayer_broj_mogucih_poteza = len(myPlayer.moguci_potezi)
        oppPlayer_broj_mogucih_poteza = len(oppPlayer.moguci_potezi)
        if(myPlayer_broj_mogucih_poteza > oppPlayer_broj_mogucih_poteza):
            return (100.0 * myPlayer_broj_mogucih_poteza) / (myPlayer_broj_mogucih_poteza + oppPlayer_broj_mogucih_poteza)
        elif myPlayer_broj_mogucih_poteza < oppPlayer_broj_mogucih_poteza:
            return -(100.0 * oppPlayer_broj_mogucih_poteza) / (myPlayer_broj_mogucih_poteza + oppPlayer_broj_mogucih_poteza)
        return 0
        
    def heuristika(self, tabla, myPlayer, oppPlayer):
        ruf = self.izracunaj_razliku_u_figurama(myPlayer, oppPlayer)
        vrp = self.izracunaj_vrednosti_polja_i_ivicnih(tabla, myPlayer, oppPlayer)[0]
        iv = self.izracunaj_vrednosti_polja_i_ivicnih(tabla, myPlayer, oppPlayer)[1]
        c = self.izracunaj_zauzetost_coskova(tabla, myPlayer, oppPlayer)
        poz = self.izracunaj_pozicije_do_coskova(tabla, myPlayer, oppPlayer)
        m = self.mobilnost(myPlayer, oppPlayer)
        rezultat = (10 * ruf) + (801.724 * c) + (382.026 * poz) + (78.922 * m) + (74.396 * iv) + (10 * vrp)
        return rezultat