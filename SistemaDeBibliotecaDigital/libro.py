# En el archivo libro.py
from material import Material # Asegúrate de que importas la clase base

class Libro(Material):
    def __init__(self, titulo, autor, precio, paginas):
        super().__init__(titulo, autor, precio) 
        self.paginas = paginas

    def descripcion(self):
        super().descripcion()
        print(f"Libro: -Titulo: {self.titulo}, -Autor: {self.autor}, paginas: {self.paginas}, precio ${self.get_precio} ")