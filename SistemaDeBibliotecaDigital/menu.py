from biblioteca import Biblioteca

uso_biblioteca = Biblioteca()

def llamado_menu():
    menu()
    opciones()

def menu():
    print("Bienvenidos a la biblioteca")
    print("Menu")
    print("1. Ingresar Articulos")
    print("2. Editar articulos")
    print("3. Mostrar catalogo")
    print("4. Salir")

def opciones():
    while True: # Bucle para que el menú se repita
        try:
            opcion = int(input("Ingrese un número: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue

        if opcion == 1:
            print("tipo de articulos")
            print("libro")
            print("revista")
            print("periodico")
            tipo_articulo = input("Ingrese el nombre del tipo de artículo (ej. 'libro'): ").lower()

            if tipo_articulo in ["libro", "revista", "periodico"]:
                titulo = input("Ingrese el título: ")
                autor = input("Ingrese el autor: ")
                
                # Conversión a float para el precio
                try:
                    precio = float(input("Ingrese el precio: "))
                except ValueError:
                    print("Precio inválido. Por favor, ingrese un número.")
                    continue
                
                datos = {
                    'titulo': titulo,
                    'autor': autor,
                    'precio': precio
                }

                if tipo_articulo == "libro":
                    # Conversión a int para las páginas
                    try:
                        paginas = int(input("Ingrese la cantidad de páginas: "))
                        datos['paginas'] = paginas
                    except ValueError:
                        print("Páginas inválidas. Por favor, ingrese un número entero.")
                        continue

                elif tipo_articulo == "revista":
                    editorial = input("Ingrese la editorial: ")
                    datos['editorial'] = editorial

                elif tipo_articulo == "periodico":
                    # La fecha puede ser una cadena, no hay problema
                    fecha_publicacion = input("Ingrese la fecha de la publicación: ")
                    datos['fecha_publicacion'] = fecha_publicacion
                
                # Aquí se usa el diccionario 'datos' genérico
                uso_biblioteca.agregar_material(tipo_de_material=tipo_articulo, datos=datos)

            else:
                print("Ingrese un artículo válido.")

        elif opcion == 2:
            nombre_articulo = input("Ingrese el nombre del artículo a editar: ")
            # Conversión a float para el nuevo precio
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio: $"))
                uso_biblioteca.set_precio(nombre_articulo, nuevo_precio)
            except ValueError:
                print("Precio inválido. Por favor, ingrese un número.")
        
        elif opcion == 3:
            uso_biblioteca.mostrar_catalogo()

        elif opcion == 4:
            print("Saliendo de la aplicación.")
            break # Termina el bucle y el programa

        else:
            print("Ingrese un número válido.")
        
        llamado_menu() # Llama al menú de nuevo para que se repita

