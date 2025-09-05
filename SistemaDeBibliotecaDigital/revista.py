from material import Material

class Revista(Material):
    def __init__(self, titulo, autor, precio, editorial):
        super().__init__(titulo, autor, precio)
        self.editorial = editorial

    def descripcion(self):
        super().descripcion()
        print(f"Revista: -Titulo: {self.titulo}, -Autor: {self.autor}, Editorial: {self.editorial}, precio ${self.get_precio} ")