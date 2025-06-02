# Utwórz klasę Coin. Konstruktor tej klasy powinien przyjmować jeden parametr denomination
# (nominał monety - liczba całkowita) i tworzyć dwa atrybuty publiczne:
# - side - utrzymujący aktualną stronę monety (wartość domyślna to "orzeł");
# - denomination - nomianł monety inicjalizowany wartością parametru konstruktora.

import random

class Coin:
    def __init__(self, denomination):
        self.side = "orzeł"
        self.denomination = denomination

# Zdefiniuj dwie metody:
# - throw() - losowo "zmienia" stronę monety ("orzeł" lub "reszka");
# - __str__() - wyświetla tekstową reprezentację obiektu (strona monety)

    def throw(self):
        self.side = random.choice(["orzeł", "reszka"])

    def __str__(self):
        return f"Moneta {self.denomination} zł\tWylosowałeś: {self.side}"
    
# Wykonaj następujące dwa zadania:
# a) Utwórz kilka obiektów klasy Coin i wywołaj ich metody oraz wykonaj symulację piętnastu
#    rzutów monetą.

jeden_zloty = Coin(1)
dwa_zlote = Coin(2)
piec_zloty = Coin(5)
n = 0
portfel = [jeden_zloty, dwa_zlote, piec_zloty]

for moneta in portfel:
    print(f"Rzuty monetą {moneta.denomination} zł")
    for i in range(15):
        moneta.throw()
        print(moneta)

# Napisz porgram, który będzie symulował pewną grę hazardową.
# Program powinien tworzyc trzy instancje klasy Coin reprezentujące monety
# o nominałach 1 zł, 2 zł i 5 zł. Początkowe saldo gry powinno być równe 0 zł.
# W każdej kolejce program powinien wykonywać rzut trzema monetami i dodawać do salda
# ich wartości, jeżeli n danej monecie wypadnie orzeł. Gra powinna się kończyć wtedy,
# gdy saldo będzie równe lub większe 20 zł. Saldo równe dokładnie 20 zł oznacza wygraną,
# a większe przegraną. Wykonaj np. 100 symulacji gry i zlicz przegrane i wygrane.

print("=" * 40)
print(" " * 10 + "🎰 GRA HAZARDOWA 🎰")
print("=" * 40)

def gra_hazardowa(ilosc_symulacji):
    moneta1 = Coin(1)
    moneta2 = Coin(2)
    moneta5 = Coin(5)
    wygrane = 0
    przegrane = 0
    

    for i in range(ilosc_symulacji):
        saldo = 0
        while (saldo < 20):
            moneta1.throw()
            moneta2.throw()
            moneta5.throw()

            if moneta1.side == "orzeł":
                saldo += 1
            
            if moneta2.side == "orzeł":
                saldo += 2

            if moneta5.side == "orzeł":
                saldo += 5

        if saldo != 20:
            przegrane += 1
        else:
            wygrane += 1

    print(f"Rozegrano {ilosc_symulacji} gier...\nIlość wygranych: {wygrane}\nIlość przegranych: {przegrane}")

gra_hazardowa(100)
    
    

