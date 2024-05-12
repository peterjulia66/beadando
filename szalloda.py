class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, wifi):
        super().__init__(ar, szobaszam)
        self.wifi = wifi

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, erkely):
        super().__init__(ar, szobaszam)
        self.erkely = erkely

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

def foglalas(self, szoba_szam, datum):
    for szoba in self.szobak:
        if szoba.szobaszam == szoba_szam:
            return szoba.ar
    return None

def lemondas(self, foglalas):
    self.foglalasok.remove(foglalas)

def osszes_foglalas(self):
    for foglalas in self.foglalasok:
        print(f"Foglalás: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

def felhasznaloi_interfesz():
    print("Válassz műveletet:")
    print("1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")

def foglalas(self, szoba_szam, datum):
    for szoba in self.szobak:
        if szoba.szobaszam == szoba_szam:
            if self.is_datum_valid(datum) and self.is_szoba_available(szoba_szam, datum):
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
            else:
                return None
    return None

def is_datum_valid(self, datum):

def is_szoba_available(self, szoba_szam, datum):

def lemondas(self, foglalas):
    if foglalas in self.foglalasok:
        self.foglalasok.remove(foglalas)
    else:
        print("Nem létező foglalás!")

def feltolt_system():
    szalloda = Szalloda("Példa Szálloda")

    szoba1 = EgyagyasSzoba(10000, 101, True)
    szoba2 = EgyagyasSzoba(12000, 102, False)
    szoba3 = KetagyasSzoba(15000, 201, True)

    szalloda.add_szoba(szoba1)
    szalloda.add_szoba(szoba2)
    szalloda.add_szoba(szoba3)

    foglalas1 = Foglalas(szoba1, "2022-10-01")
    foglalas2 = Foglalas(szoba2, "2022-10-02")
    foglalas3 = Foglalas(szoba2, "2022-10-03")
    foglalas4 = Foglalas(szoba3, "2022-10-04")
    foglalas5 = Foglalas(szoba3, "2022-10-05")

    szalloda.foglalasok = [foglalas1, foglalas2, foglalas3, foglalas4, foglalas5]

    return szalloda