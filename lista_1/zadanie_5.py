# Napisz klasę Time, która reprezentuje obiekt czasu. Klasa powinna posiadać następujące metody i właściwości:
# - konstruktor klasy o trzech parametrach: hour, minute, second (o wartościach domyślnych równych 0),
#   który tworzy i inicjalizuje trzy atrybuty publiczne odpowiadające parametrom;

class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

# - właściwości, które zarządzają każdym z trzech atrybutów i kontrolują ich poprawność:
#   - hour - liczba całkowita z zakresu 0-23;
#   - minute - liczba całkowita z zakresu 0-59;
#   - second - liczba całkowita z zakresu 0-59.

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if not isinstance(value, int):
            raise TypeError("Godzina musi być liczbą całkowitą!")
        
        if not (0 <= value <= 23):
            raise ValueError("Godzina musi być liczbą z zakresu 0-23")
        
        self._hour = value  

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if not isinstance(value, int):
            raise TypeError("Minuta musi być liczbą całkowitą!")
        
        if not (0 <= value <= 59):
            raise ValueError("Minuta musi być liczbą z zakresu 0-59")
        
        self._minute = value 

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        if not isinstance(value, int):
            raise TypeError("Sekunda musi być liczbą całkowitą!")
        
        if not (0 <= value <= 59):
            raise ValueError("Sekunda musi być liczbą z zakresu 0-59")
        
        self._second = value

# - metoda set_time() - ustawia wskazania godzin, minut i sekund wartościami jej przekazanymi (o wartościach domyślnych równych 0);

    def set_time(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second


# - metoda __repr__() - zwraca reprezentację tekstową wg. repr();

    def __repr__(self):
        return f"Time(hour={self.hour}, minute={self.minute}, second={self.second})"
    
# - metoda __str__() - zwraca wskazanie czasu w formacie 12-godzinnym (z sufiksem PM lub AM)

    def __str__(self):
        if self.hour == 0:
            hour12 = 12
            suffix = "AM"
        elif 1 <= self.hour <= 11:
            hour12 = self.hour
            suffix = "AM"
        elif self.hour == 12:
            hour12 = 12
            suffix = "PM"
        else:
            hour12 = self.hour - 12
            suffix = "PM"

        return f"{hour12:02d}:{self.minute:02d}:{self.second:02d} {suffix}"

t1 = Time(5, 10, 15)
print(t1)
print(repr(t1))
print("Zmiana godziny na 22:45:11")
t1.set_time(23, 45, 11)
print(t1)
print(repr(t1))

