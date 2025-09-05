class Material:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio


    def	get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_valor):
        if nuevo_valor > 0:
            self.__precio = nuevo_valor
        else:
            print("El precio debe ser mayor que 0.")

    def descripcion(self):
        print(f"Material: -Titulo: {self.titulo}, -Autor: {self.autor}")