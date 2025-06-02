# Utwórz klasę Dice reprezentującą kostkę do gry. Zdefiniuj w tej klasie
# następujące metody:
# - konstrukt klasy powinien tworzyc dwa atrybuty prywatne:
#       - sides - liczba ścian kostki (inicjalizowany wartością parametru konstrukora);
#       - value - wylosowana liczba oczek (o wartości początkowej równej np. None).
# - metoda roll() - wykonuje rzut kostką i wynik rzutu przypisuje do atrybutu value;
# - get_sides() - zwraca liczbę ścianek;
# - get_value() - zwraca liczbę oczek na kostce;
# - __str__() - wyświetla wartości atrybutów;

import random

class Dice:
    def __init__(self, sides):
        self.__sides = sides
        self.__value = None

    def roll(self):
        self.__value = random.randint(1, self.__sides)

    def get_sides(self):
        return self.__sides
    
    def get_value(self):
        return self.__value
    
    def __str__(self):
        return f"Kostka do gry, która posiada {self.__sides} ścian zatrzymała się na następującej liczbie oczek {self.__value}"
    
# Napisz program w którym użytkownik będzie grał w popularną grę "Oczko", ale z wykorzystaniem
# dwóch sześciennych kostek. Gracz będzie rzucał kostkami starając się uzyskać większą liczbę
# punktów od ukrytych punktów komputera, ale nie większą niż 21. Sugestie dotyczące gry:
#
# - Każda kolejka gry powinna być obiegiem pętli, 
#   powtarzanej dotąd, aż gracz zrezygnuje z rzucania 
#   lub gdy suma punktów będzie większa niż 21.
#
# - Na początku każdej kolejki gracz powinien być pytany,
#   czy chce kontynuować rzucanie i sumować punkty.
#
# - W każdej kolejce program powinien symulować rzut 
#   dwiema sześciennymi kostkami. Najpierw rzuca 
#   komputer, a następnie gracz decyduje, czy rzucić
#   jego kostkami.
#
# - Program powinien sumować punkty gracza i komputera
#   (punkty komputera są ukryte do końca gry).
#
# - Po zakończeniu pętli program ujawnia punkty komputera.
#   Gracz wygrywa, jeżeli zdobył więcej punktów niż komputer,
#   ale nie więcej niż 21.

def oczko():
    kostka_1_gracz = Dice(6)
    kostka_2_gracz = Dice(6)
    kostka_1_pc = Dice(6)
    kostka_2_pc = Dice(6)

    suma_oczek_gracz = 0
    suma_oczek_pc = 0
    zakonczyc = False
    licznik_do_rund = 1

    print("No to zaczynamy...")
    kostka_1_gracz.roll()
    kostka_2_gracz.roll()
    kostka_1_pc.roll()
    kostka_2_pc.roll()

    suma_oczek_pc += kostka_1_pc.get_value() + kostka_2_pc.get_value()
    suma_oczek_gracz += kostka_1_gracz.get_value() + kostka_2_gracz.get_value()

    print(f"Liczba punktów z kostki pierwszej: {kostka_1_gracz.get_value()}")
    print(f"Liczba punktów z kostki drugiej: {kostka_2_gracz.get_value()}")
    print(f"Liczba punktów po rundzie {licznik_do_rund}: {suma_oczek_gracz}")

    while suma_oczek_gracz <= 21 and not zakonczyc:
        operator = input("Czy chcesz kontynuować grę (t/n): ")
        if operator == "t":
            licznik_do_rund += 1
            kostka_1_gracz.roll()
            kostka_2_gracz.roll()
            kostka_1_pc.roll()
            kostka_2_pc.roll()

            suma_oczek_pc += kostka_1_pc.get_value() + kostka_2_pc.get_value()
            suma_oczek_gracz += kostka_1_gracz.get_value() + kostka_2_gracz.get_value()

            print(f"Liczba punktów z kostki pierwszej: {kostka_1_gracz.get_value()}")
            print(f"Liczba punktów z kostki drugiej: {kostka_2_gracz.get_value()}")
            print(f"Liczba punktów po rundzie {licznik_do_rund}: {suma_oczek_gracz}")
        elif operator == "n":
            zakonczyc = True
        else:
            print("Wprowadź 't' jeśli chcesz kontynuować, lub 'n' jeśli nie chcesz.")

    print("\n--- KONIEC GRY ---")
    print(f"Twoje punkty: {suma_oczek_gracz}")
    print(f"Punkty komputera: {suma_oczek_pc}")

    if suma_oczek_gracz > 21:
        print("Przegrałeś - masz więcej niż 21 punktów!")
    elif suma_oczek_pc > 21:
        print("Komputer przekroczył 21! Wygrałeś!")
    elif suma_oczek_gracz > suma_oczek_pc:
        print("Gratulacje! Wygrałeś!")
    elif suma_oczek_gracz < suma_oczek_pc:
        print("Niestety, tym razem komputer był lepszy...")
    else:
        print(f"Tym razem padł remis! Zdobyliście po {suma_oczek_gracz} punktów.")

oczko()


        
