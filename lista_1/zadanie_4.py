# Napisz klasę Matrix, która reorezentuje macierz o zadanych wymiarach.
# Zdefiniuj w tejk klasie następujące metody i właściwości:
# - konstruktor klasy, który powinien tworzyć trzy atrybuty prywatne:
#   - _row - liczba wierszy macierzy (inicjalizowany wartością parametru konstruktora);
#   - _col - liczba kolumn macierzy (inicjalizowany wartością parametru konstruktora);
#   - _matrix - lista list reprezentująca macierz (wypełniana jednakowymi wartościami początkowymi value - parametr konstruktora
#     o wartości domyślnej None).

class Matrix:
    def __init__(self, row, col, value = None):
        self._row = row
        self._col = col
        self._matrix = [[value for _ in range(col)] for _ in range(row)]  

# - właściwość size() zwracającą wymiar macierzy jako krotkę;

    @property
    def size(self):
        return (self._row, self._col)

# - metoda prywatna _check_index() która zgłasza wyjątek IndexError jeżeli przekazane jej wartości wiersza i kolumny
#   są poza zakresem macierzy;

    def _check_index(self, row, col):
        if not (0 <= row < self._row):
            raise IndexError(f"Wiersz {row} poza zakresem (0–{self._row - 1})")
        if not (0 <= col < self._col):
            raise IndexError(f"Kolumna {col} poza zakresem (0–{self._col - 1})")
        
# - get_cell() - metoda zwracająca element macierzy o zadanych współrzędnych - metoda powinna korzystać z metody _check_index()
#   w celu sprawdzenia poprawności indeksów;

    def get_cell(self, row, col):
        self._check_index(row, col)
        return self._matrix[row][col]
    
# - set_cell() pozwalająca zmienić wartość komórki macierz o zadanych współrzędnych - metoda powinna korzystać z metody _check_index()
#   w celu sprawdzenia poprawności indeksów;

    def set_cell(self, row, col, value):
        self._check_index(row, col)
        self._matrix[row][col] = value

# - metoda __str__() wyświetlająca macierz w klasyczny sposób.

    def __str__(self):
        result = ""
        for row in self._matrix:
            result += " ".join(str(cell) for cell in row) + "\n"
        return result.strip() 