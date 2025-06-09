# Napisz program symulujący prosty notatnik. Program powinien składać się z modułu zawierającego klasy Note i Notebook, a także klasy
# Menu, która obsługuje interakcję z użytkownikiem.
#
# Klasa Note reprezentuje pojedynczą notatkę i powinna posiadać następujące atrybuty: 
#   text - tekst notatki, przekazany jako argument konstruktora; 
#   tag - etykieta (tag) przypisana do notatki (ustawiana automatycznie);
#   ID - unikalny numer notatki w ramach notatnika (generowany automatycznie, np. poprzez atrybut zliczający utworzone instancje).
# Klasa powinna także zawierać metodę match(self, query), która sprawdza, czy tekst notatki lub jej etykieta zawiera podane słowo
# kluczowe query. Zwraca wartość logiczną True lub False.

class Note:
    _id_counter = 1

    def __init__(self, text):
        self.text = text
        self.ID = Note._id_counter
        Note._id_counter += 1
        self.tag = self._generate_tag(text)

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        if len(value) < 5:
            raise ValueError("Nie zaśmiecaj sobie notatnika krótkimi notkami, wprowadź więcej niż 5 znaków")
        
        self._text = value

    def _generate_tag(self, text):
        short = text[:10]
        return short + "..." if len(text) > 10 else short + "..."

    def match(self, query):
        return query.lower() in self._text.lower() or query.lower() in self.tag.lower()

# Klasa Notebook reprezentuje zbiór notatek i powinna zawierać atrybut notes, czyli listę przechowującą obiekty klasy Note.
# Klasa powinna implementować następujące metody:
# - new_note(text, tag) - dodaje nową notatkę do listy;
# - modify_text(ID, new_text) - zmienia treść notatki o podanym ID;
# - modify_tag(ID, new_tag) - zmienia etykietę notatki o podanym ID;
# - search(query) - zwraca listę notatek zawierajacych dany ciąg znaków w treści lub etykiecie. Jeśli brak wyników, zwraca pustą listę.

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, text):
        note = Note(text)
        self.notes.append(note)

    
    

