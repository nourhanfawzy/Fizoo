from models import Book
from autofixture import generators, register, AutoFixture

class BookAutoFixture(AutoFixture):
    field_values = {
        'name': generators.StaticGenerator('trial static name'),
    }

register(Book, BookAutoFixture)