# Utwórz klasę Account reprezentująca saldo konta bankowego. Zdefinuj w tej kalsie następujące metody:
# - kontstruktor klasy, który tworzy atrybuty balance i name inicjalizowane wartościami parametrów konstruktora -
# jeżeli wartość parametru balance jest ujemna program powinien zgłaszać błąd (wyjątek ValueError z wartością np. 'Saldo 
# początkowe nie może być ujemne.')
#
# - metoda deposit(), która zwiększa saldo konta o przekazaną jej wartość - metoda powinna zgłaszać błąd,
# gdy wpłacona kwota jest ujemna (wyjątek ValueError z wartością np. 'Nie mozna wpłacić ujemnej kwoty.');
#
# - metoda take(), która zmniejsza saldo konta o podaną wartość lub zgłasza błąd o braku środków na koncie
# (wyjątek ValueError z wartością np. 'Brak środków na koncie.');
# 
# - __str__() - wyświetla m.in. wartość atrybutu balance i nazwę konta.
#
# Przetestuj klasę w prostym programie z obsługą wyjątków

class Account:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

        if balance < 0:
            raise ValueError("Saldo początkowe nie może być ujemne.")
    

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Nie można wpłacić ujemnej kwoty.")

        self.balance += amount

    def take(self, amount):
        if amount > self.balance:
            raise ValueError("Brak środków na koncie")

    def __str__(self):
        return f"Nazwa konta:\t{self.name}\nStan konta:\t{self.balance} zł"
    

konto1 = Account(1000, "Marcin")
print(konto1)
print("Następuje wpłata 250 zł")
konto1.deposit(250)
print(konto1)
print("Następuje pobranie 1000 zł")
konto1.take(1000)
print(konto1)
print("=========================")
print("Testowanie wyjątków")
print("=========================")
# konto2 = Account(-1, "Wojtek")
# konto1.deposit(-100)
konto1.take(1000000)