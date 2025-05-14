from othello import Othello

def meni():
    print("\033c")
    print("=" * 10 + "OTHELLO" + "=" * 10)
    print("(1) Započnite igru")
    print("(2) Izađite iz aplikacije")
    print("=" * 26)

if __name__ == '__main__':
    while True:
        meni()
        unos = ''
        while unos != '1' and unos != '2':
            unos = input(">> ").strip()
        if unos == '1':
            print("\033c")
            izbor = ""
            while izbor != "CRNI" and izbor != "BELI":
                izbor = input("Da li želite da igrate kao beli ili crni? (crni/beli): ").strip().upper()
            if izbor == "CRNI":
                igra = Othello("⚫️", "⚪️")
                igra.igraj(izbor)
            else:
                igra = Othello("⚪️", "⚫️")
                igra.igraj(izbor)
        else:
            exit()

