class Profesor:
    BD = {}

    @classmethod
    def MenuProfesores(cls):
        while True:
            print("------PROFESORES------")
            print("1. Añadir Profesor")
            print("2. Ver lista de profesores")
            print("3. Actualizar información")
            print("4. Eliminar profesor")
            print("5. Volver al menú principal")

            opcion = input("¿Qué quieres hacer?: ")

            if opcion == '1':
                print("-----Añadir Profesor-----")
                id_profesor = int(input("Escribe el ID del profesor: "))
                nombre = input("Escribe el nombre del profesor: ")
                departamento = input("Escribe el departamento al que pertenece el profesor: ")

                if id_profesor in cls.BD:
                    print("Ya existe un profesor con ese ID.")
                    continue
                else:
                    cls.BD[id_profesor] = {'nombre': nombre, 'departamento': departamento}
                    print("¡Profesor añadido correctamente!\n")

            elif opcion == '2':
                print("-----Lista de Profesores-----")
                for id_profesor, datos_profesor in cls.BD.items():
                    print("ID:", id_profesor)
                    print("Nombre:", datos_profesor['nombre'])
                    print("Departamento:", datos_profesor['departamento'], "\n")

            elif opcion == '3':
                print("-----Actualizar Información-----")
                id_modificar = int(input("Escriba el ID del profesor que desea actualizar: "))
                if id_modificar not in cls.BD:
                    print("El profesor con ese ID no existe.")
                    continue

                nuevo_nombre = input("Escriba el nuevo nombre: ")
                nuevo_departamento = input("Escriba el nuevo departamento: ")

                cls.BD[id_modificar]['nombre'] = nuevo_nombre
                cls.BD[id_modificar]['departamento'] = nuevo_departamento
                print("Información del profesor actualizada correctamente.\n")

            elif opcion == '4':
                print("-----Eliminar Profesor-----")
                id_eliminar = int(input("Escriba el ID del profesor que desea eliminar: "))
                if id_eliminar not in cls.BD:
                    print("El profesor con ese ID no existe.")
                    continue

                del cls.BD[id_eliminar]
                print("Profesor eliminado correctamente.\n")

            elif opcion == '5':
                print("Volviendo al Menú Principal")
                break

            else:
                print("Opción inválida, por favor intente de nuevo.")


if __name__ == "__main__":
    Profesor.MenuProfesores()
