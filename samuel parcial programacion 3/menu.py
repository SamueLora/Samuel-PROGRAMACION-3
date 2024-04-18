from estudiantes import estudiante

def MenuPrincipal():
    while True:
        print("------MENÚ PRINCIPAL------")
        print("1. Estudiantes")
        print("2. Salir")
        
        opcion= input("¡Elije una opción!: ")
        
        if opcion=='1':
            e= estudiante
            print(e.MenuEstudiantes())
        
        elif opcion=='2':
            print("Adios, ¡Vuelva Pronto!")
            break
        else:
            print("Escribe un numero que esté dentro de las opciones: ")
            
MenuPrincipal()