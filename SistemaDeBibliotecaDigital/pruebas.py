from biblioteca import Biblioteca


if __name__ == '__main__':
    mi_automotora = Biblioteca()


    nuevaRevista = {
                'titulo': "titulo",
                'autor':"autor",
                'precio':10000,
                'editorial':"editorial"
            }
    

    mi_automotora.agregar_material('revista', nuevaRevista)

    

    mi_automotora.mostrar_catalogo()