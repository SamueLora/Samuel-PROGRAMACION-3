class Asignatura:
    BD = {}

    @classmethod
    def MenuAsignaturas(cls):
        while True:
            print("------ASIGNATURAS------")
            print("1. Añadir Asignatura")
            print("2. Ver lista de asignaturas")
            print("3. Actualizar información")
            print("4. Eliminar asignatura")
            print("5. Volver al menú principal")

            opcion = input("¿Qué quieres hacer?: ")

            if opcion == '1':
                print("-----Añadir Asignatura-----")
                id_asignatura = int(input("Escribe el ID de la asignatura: "))
                nombre = input("Escribe el nombre de la asignatura: ")
                creditos = int(input("Escribe la cantidad de créditos de la asignatura: "))

                if id_asignatura in cls.BD:
                    print("Ya existe una asignatura con ese ID, intente con otro.")
                    continue
                else:
                    cls.BD[id_asignatura] = {'nombre': nombre, 'creditos': creditos}
                    print("¡Asignatura añadida correctamente!\n")

            elif opcion == '2':
                print("-----Lista de Asignaturas-----")
                for id_asignatura, datos_asignatura in cls.BD.items():
                    print("ID:", id_asignatura)
                    print("Nombre:", datos_asignatura['nombre'])
                    print("Créditos:", datos_asignatura['creditos'], "\n")

            elif opcion == '3':
                print("-----Actualizar Información-----")
                id_modificar = int(input("Escriba el ID de la asignatura que desea actualizar: "))
                if id_modificar in cls.BD:
                    nombre_mod = input("Escriba el nuevo nombre: ")
                    creditos_mod = int(input("Escriba la nueva cantidad de créditos: "))

                    cls.BD[id_modificar]['nombre'] = nombre_mod
                    cls.BD[id_modificar]['creditos'] = creditos_mod

                    print("Información de la asignatura actualizada correctamente.\n")
                else:
                    print("La asignatura con ese ID no existe.")

            elif opcion == '4':
                print("-----Eliminar Asignatura-----")
                id_eliminar = int(input("Escriba el ID de la asignatura que desea eliminar: "))
                if id_eliminar in cls.BD:
                    cls.BD.pop(id_eliminar)
                    print("Asignatura eliminada correctamente.\n")
                else:
                    print("La asignatura con ese ID no existe.")

            elif opcion == '5':
                print("Volviendo al Menú Principal")
                break

            else:
                print("Opción inválida, por favor intente de nuevo.")


if __name__ == "__main__":
    Asignatura.MenuAsignaturas()
