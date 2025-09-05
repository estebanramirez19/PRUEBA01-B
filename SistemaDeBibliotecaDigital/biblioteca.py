from libro import Libro
from periodico import Periodico
from revista import Revista

class Biblioteca:
    def __init__(self):
        self.materiales = []

    def agregar_material(self, tipo_de_material, datos):
        if tipo_de_material.lower() == "libro":
            nuevo_libro = Libro(
                titulo=datos['titulo'],
                autor=datos['autor'],
                precio=datos['precio'],
                paginas=datos['paginas']
            )
            # Línea corregida:
            self.materiales.append(nuevo_libro)
            print(f"Se ha agregado un libro con exito")

        elif tipo_de_material.lower() == "revista":
            nueva_revista = Revista( 
                titulo= datos["titulo"],
                autor=datos["autor"],
                precio=datos["precio"],
                editorial=datos["editorial"]
            )
            # Línea corregida:
            self.materiales.append(nueva_revista)
            print(f"Se ha agregado una revista con exito")

        elif tipo_de_material.lower() == "periodico":
            nuevo_periodico = Periodico( # Cambié "nueva_periodico" a "nuevo_periodico"
                titulo=datos["titulo"],
                autor=datos["autor"],
                precio=datos["precio"],
                fecha_publicacion=datos["fecha_publicacion"]
            )
            # Línea corregida:
            self.materiales.append(nuevo_periodico)
            print(f"Se ha agregado un periodico con exito") # Corregí el mensaje

        else:
            print("Escriba un tipo de material valido")

    def mostrar_catalogo(self):
        if not self.materiales:
            print("No hay articulos para mostrar.")
            return

        total_precio = 0  
        print("\n--- Listado Del Catalogo---")
        for articulo in self.materiales:
            print(f"{articulo.descripcion()}")
            total_precio += articulo.get_precio()

        print(f"\n--- Precio Total Del Catalogo: ${total_precio} ---")

    def set_precio(self, titulo_material, nuevo_precio):
        encontrado = False
        for articulo in self.materiales:
            if articulo.titulo == titulo_material:
                articulo.precio = nuevo_precio
                print(f"El precio del artículo '{titulo_material}' se ha actualizado a ${nuevo_precio}.")
                encontrado = True
                break
        if not encontrado:
            print(f"Error: No se encontró ningún artículo con el título '{titulo_material}'.")