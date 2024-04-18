class Estudiante:
    BD = {}

    @classmethod
    def MenuEstudiantes(cls):
        while True:
            print("------ESTUDIANTES------")
            print("1. Añadir Estudiante")
            print("2. Ver lista de estudiantes")
            print("3. Actualizar información")
            print("4. Eliminar estudiante")
            print("5. Volver al menú principal")

            opcionestu = input("¿Qué quieres hacer?: ")

            if opcionestu == '1':
                print("-----Añadir estudiante-----")
                id_estudiante = int(input("Escribe el ID del estudiante: "))
                nombre = input("Escribe el nombre completo del estudiante: ")
                edad = int(input("Escribe la edad del estudiante: "))

                if id_estudiante in cls.BD:
                    print("Ya existe un estudiante con esa ID, intente con otra: ")
                    continue
                else:
                    cls.BD[id_estudiante] = [nombre, edad]
                    print("¡Datos Guardados Correctamente!\n")

            elif opcionestu == '2':
                print("-----Lista de Estudiantes-----")
                for id_estudiante, datos_estudiante in cls.BD.items():
                    print("ID:", id_estudiante)
                    print("Nombre:", datos_estudiante[0])
                    print("Edad:", datos_estudiante[1], "\n")

            elif opcionestu == '3':
                print("-----Actualizar Información-----")
                id_modificar = int(input("Escriba el ID del estudiante que desea actualizar: "))
                nombre_mod = input("Escriba el nuevo nombre: ")
                edad_mod = input("Escriba la nueva edad: ")

                cls.BD[id_modificar][0] = nombre_mod
                cls.BD[id_modificar][1] = edad_mod

                print("Datos Modificados Exitosamente\n")

            elif opcionestu == '4':
                print("-----Eliminar Estudiante-----")
                id_eliminar = int(input("Escriba el ID del estudiante que desea eliminar: "))
                cls.BD.pop(id_eliminar)
                print("Estudiante eliminado exitosamente!\n")

            elif opcionestu == '5':
                print("Volviendo al Menu Principal")
                break

            else:
                print("Dato inválido, escribe otro: ")
