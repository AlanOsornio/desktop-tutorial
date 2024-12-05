# Clase inical
class BookSystem:
    def __init__(self):
        self._data = []  # Encapsulamiento

    def get_data(self):
        return self._data

    def add_data(self, item):
        self._data.append(item)

# Clase Catalogue hereda de BookSystem
class Catalogue(BookSystem):
    def search_author(self, author):
        # Encapsulamiento
        return [book for book in self._data if book['author'] == author]

    def update_catalogue(self, book):
        self.add_data(book)  # Reutilización mediante herencia

# Clase AvailableBooks hereda de BookSystem
class AvailableBooks(BookSystem):
    def check_availability(self, title):
        # Encapsulamiento: Verifica disponibilidad de libros
        return title in self._data

# Clase User con polimorfismo para diferentes tipos de usuarios
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        # Polimorfismo: Adaptación del método para usuarios
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
        else:
            raise Exception(f"Book '{book}' already borrowed by {self.name}.")

# Clase Loan con polimorfismo 
class Loan:
    def __init__(self):
        self._loans = []  # Encapsulamiento

    def checkout(self, user, book):
        try:
            # Polimorfismo: Diferentes implementaciones según el tipo de usuario
            user.borrow_book(book)
            self._loans.append({'user': user.name, 'book': book})
        except Exception as e:
            print(f"Error: {e}")  # Manejo de errores

catalogue = Catalogue()
available_books = AvailableBooks()
loan_system = Loan()

# Agrega los libros disponibles
catalogue.update_catalogue({'title': 'El señor de los anillos', 'author': 'Placido Lopez'})
available_books.add_data('Book1')

#Creacion de usuario y prestamo
user = User('Josue')

if available_books.check_availability('Book1'):
    loan_system.checkout(user, 'Book1')
    print(f"{user.name} ha tomado prestado el libro: 'Book1'.")
else:
    print("The book is not available.")
