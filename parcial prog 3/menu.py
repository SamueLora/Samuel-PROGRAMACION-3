from estudiantes import Estudiante
from asignaturas import Asignatura
from profesores import Profesor
from carrera import Carrera

def MenuPrincipal():
    while True:
        print("------MENÚ PRINCIPAL------")
        print("1. Estudiantes")
        print("2. Asignaturas")
        print("3. Profesores")
        print("4. Carrera")
        print("5. Salir")
        opcion = input("¡Elije una opción!: ")

        if opcion == '1':
            Estudiante.MenuEstudiantes()

        elif opcion== '2':
            Asignatura.MenuAsignaturas()
        
        elif opcion== '3':
            Profesor.MenuProfesores()
        
        elif opcion== '4':
            Carrera.MenuCarreras()
            
        elif opcion == '5':
            print("Adios, ¡Vuelve Pronto!")
            break
        else:
            print("Escribe un numero que esté dentro de las opciones: ")
    
