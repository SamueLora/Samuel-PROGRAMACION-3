class Carrera:
    BD = {}

    @classmethod
    def MenuCarreras(cls):
        while True:
            print("------CARRERAS------")
            print("1. Añadir Carrera")
            print("2. Ver lista de carreras")
            print("3. Actualizar información")
            print("4. Eliminar carrera")
            print("5. Volver al menú principal")

            opcion = input("¿Qué quieres hacer?: ")

            if opcion == '1':
                print("-----Añadir Carrera-----")
                codigo_carrera = input("Escribe el código de la carrera: ")
                nombre_carrera = input("Escribe el nombre de la carrera: ")
                duracion = input("Escribe la duración de la carrera: ")

                if codigo_carrera in cls.BD:
                    print("Ya existe una carrera con ese código.")
                    continue
                else:
                    cls.BD[codigo_carrera] = {'nombre': nombre_carrera, 'duracion': duracion}
                    print("¡Carrera añadida correctamente!\n")

            elif opcion == '2':
                print("-----Lista de Carreras-----")
                for codigo_carrera, datos_carrera in cls.BD.items():
                    print("Código:", codigo_carrera)
                    print("Nombre:", datos_carrera['nombre'])
                    print("Duración:", datos_carrera['duracion'], "\n")

            elif opcion == '3':
                print("-----Actualizar Información-----")
                codigo_modificar = input("Escriba el código de la carrera que desea actualizar: ")
                if codigo_modificar not in cls.BD:
                    print("La carrera con ese código no existe.")
                    continue

                nuevo_nombre = input("Escriba el nuevo nombre: ")
                nueva_duracion = input("Escriba la nueva duración: ")

                cls.BD[codigo_modificar]['nombre'] = nuevo_nombre
                cls.BD[codigo_modificar]['duracion'] = nueva_duracion
                print("Información de la carrera actualizada correctamente.\n")

            elif opcion == '4':
                print("-----Eliminar Carrera-----")
                codigo_eliminar = input("Escriba el código de la carrera que desea eliminar: ")
                if codigo_eliminar not in cls.BD:
                    print("La carrera con ese código no existe.")
                    continue

                del cls.BD[codigo_eliminar]
                print("Carrera eliminada correctamente.\n")

            elif opcion == '5':
                print("Volviendo al Menú Principal")
                break

            else:
                print("Opción inválida, por favor intente de nuevo.")


