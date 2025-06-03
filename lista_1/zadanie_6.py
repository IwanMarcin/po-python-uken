# Napisz program, który będzie symulował opiekę nad wirtualnym zwierzakimem. W tym celu utwórz klasę Pet
# Klasa powinna posiadać metody i właściwości opisane poniżej:
# - kontruktor klasy powinien inicjalizować trzy publiczne atrybuty obiektu klasy Pet: name, hunger, tiredness
#   (zarówno głód jak i znudzenie powinny mieć na początku wartość domyślną 0 - co będzie powodowało, że na początku
#   twój zwierzak będzie w dobrym nastroju);

class Pet:
    def __init__(self, name, hunger = 0, tiredness = 0):
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness

# - za pomocą właściwości kontroluj dostęp i ustawianie atrybutu name - minimum trzyliterowy ciąg tekstowy (zawierający tylko litery);

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Imię musi być tekstem.")
        if len(value) < 3:
            raise ValueError("Imię powinno mieć co najmniej 3 litery.")
        if not value.isalpha():
            raise ValueError("Imię może zawierać TYLKO litery.")

        self._name = value

# - utwórz prywatną metodę o nazwie _passage_of_time(), która zwiększa (o jeden) poziom głodu i znudzenia zwierzaka - 
#   załóż,że czas mija dla zwierzaka tylko, gdy ten coś robi (tj. mówi, bawi się lub je);

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

# - utwórz właściwość mood() reprezentująca nastrój twojego zwierzaka - zwierzak jest szczęśliwy (suma poziomu głodu i znudzenia < 5),
#   zadowolony (suma poziomu głodu i znudzenia w zakresie od 5 do 10), podenerwowany (suma poziomu głodu i znudzenia w zakresie od
#   11 do 15) i wściekły (suma poziomu głodu i znudzenia > 15);

    @property
    def mood(self):
        if (self.hunger + self.tiredness) < 5:
            return "SZCZĘŚLIWY ❤"
        elif 5 <= (self.hunger + self.tiredness) <= 10:
            return "ZADOWOLONY 😁"
        elif 11 <= (self.hunger + self.tiredness) <= 15:
            return "PODENERWOWANY 😒"
        else:
            return "WŚCIEKŁY 🤬"
        
# - utwórz metodę talk(), która informuje jaki jest nastrój zwierzaka;
# - metoda eat() powinna zmniejszać poziom głodu zwierzaka o liczbę przekazaną poprzez parametr food (o wartości domyślnej równej 4);
# - metoda play() powinna zmniejszać poziom znudzenia zwierzaka o liczbę przekazaną poprzez parametr fun (o wartości domyślnej równej 4);
# - każda z trzech metod (talk(), eat(), play()) obiektu klasy Pet powinna wywoływać prywatną metodę _passage_of_time();
    @property
    def talk(self):
        print(f"Jestem... {self.mood}")
        self._passage_of_time()

    def eat(self, food = 4):
        self.hunger -= food
        self._passage_of_time()

    def play(self, fun = 4):
        self.tiredness -= fun
        self._passage_of_time()

# - metoda __str__() reprezentując stan zwierzaka.

    def __str__(self):
        return f"IMIĘ:\t{self.name}\nPOZIOM GŁODU 🍖:\t{self.hunger}\nPOZIOM ZNUDZENIA 😶:\t{self.tiredness}"
    
# Napisz główną funkcję programu o nazwie main(), w której nasąpi konkretyzacja obiektu klasy Pet i pojawi się menu służące
# do opieki nad zwierzakiem. Pozwól użytkownikowi na określenie ilości pożywienia podawanego zwierzakowi i czasu poświęconego
# na zabawę z nim. Wartości te powinny wpływać na szybkość spadku poziomu głodu i znudzenia u zwierzaka. Utwórz w programie
# mechanizm pozwalający na pokazanie dokładnych wartości atrybutów obiektu. Zrealizuj to poprzez wyświetlenie obiektu
# (skorzystaj z metody __str__()) po wprowadzeniu przez użytkownika specjalnej wartości (np. "xy").

def main():
    name = input("Jak chcesz nazwać swojego zwierzaka?")
    pet = Pet(name)
    print("MENU")
    print(f"Co chcesz porobić ze swoim zwierzakiem 🐶: {name}")
    print("[1] Nakarm\n[2] Pobaw się\n[3] Porozmawiaj\n[s] Pokaż stan zwierzaka\n[q] Wyjście\n\nWprowadzenie innego klawisza niż przypisane spowoduje ponowne wyświetlenie menu!")
    while True:
        action = input("Wprowadź polecenie: ")
        if action == "1":
            food = int(input("Ile jedzenia chcesz dać swojemu pupilowi? (1-5): "))
            if not 1 <= food <= 5:
                print("Próbujesz dać za dużo lub za mało jedzenia, wprowadź wartość między 1 a 5")
            elif not isinstance(food, int):
                print("Ilość jedzenia musi być liczbą całkowitą!")
            else:
                pet.eat(food)
                print("Ty: 🍖 Czas na jedzonko!")
                print("Pies: 🐶 *niucha jedzenie* 👃🍖")
                print("Pies zajada... 😋🍗🍖")
                if (pet.hunger < 15):
                    pet._passage_of_time()
        elif action == "2":
            fun = int(input("Ile atencji chcesz dać swojemu pupilowi? (1-5): "))
            if not 1 <= fun <= 5:
                print("Próbujesz dać za dużo lub za mało atencji, wprowadź wartość między 1 a 5")
            elif not isinstance(fun, int):
                print("Ilość atencji musi być liczbą całkowitą!")
            else:
                pet.play(fun)
                print("Ty: ⚾ Rzuć piłkę!")
                print("Pies: 🐶 ...")
                print("Pies biegnie... 🐾🐾🐾")
                print("Pies łapie piłkę! 🐶⚾")
                print("Pies wraca... 🐾🐾🐾")
                print("Pies oddaje piłkę! 🐶👉⚾")
                print("Dobra zabawa! 🥳")
                if (pet.tiredness < 15):
                    pet._passage_of_time()
        elif action == "3":
            pet.talk
        elif action == "s":
            print(pet)
        elif action == "q":
            break
        else:
            print("MENU")
            print(f"Co chcesz porobić ze swoim zwierzakiem 🐶: {name}")
            print("[1] Nakarm\n[2] Pobaw się\n[3] Porozmawiaj\n[s] Pokaż stan zwierzaka\n[q] Wyjście\n\nWprowadzenie innego klawisza niż przypisane spowoduje ponowne wyświetlenie menu!")

if __name__ == "__main__":
    main()