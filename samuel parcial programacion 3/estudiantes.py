class estudiante:
    
    def MenuEstudiantes():
        BD={}
        while True:
            print("------ESTUDIANTES------")
            print("1. Añadir Estudiante")
            print("2. Ver lista de estudiantes")
            print("3. Actualizar información")
            print("4. Eliminar estudiante")
            print("5. Volver al menú principal")
            
            opcionestu= input("¿Qué quieres hacer?: ")
            
            if opcionestu=='1':
                print("-----Añadir estudiante-----")
                id= int(input("Escribe el ID del estudiante: "))
                nombre= input("Escribe el nombre completo del estudiante: ")
                edad= int(input("Escribe la edad del estudiante: "))
                
                if id in BD:
                    print("Ya existe un estudiante con esa ID, intente con otra: ")
                    
                    continue
                
                else:
                    BD[id]= [nombre, edad]
                    print("¡Datos Guardados Correctamente! \n")
            
            elif opcionestu =='2':
                print("-----Lista de Estudiantes-----")
                
                for idestudiantes, datosestudiantes in BD.items():
                    print("ID:", idestudiantes)
                    print("Nombre:", datosestudiantes[0])
                    print("Edad:", datosestudiantes[1],"\n")
                    
            elif opcionestu=='3':
                print("-----Actualizar Información-----")
                
                id_a_modificar= int(input("Escriba el ID del estudiante que desea actualizar: "))
                nombre_mod= input("Escriba el nuevo nombre: ")
                edad_mod= input("Escriba la nueva edad: ")
                
                BD[id_a_modificar][0]=nombre_mod
                BD[id_a_modificar][1]=edad_mod
                
                print("Datos Modificados Exitosamente \n")
                
                print(BD[id_a_modificar])
                
            elif opcionestu=='4':
                print("-----Eliminar Estudiante-----")
                
                id_eliminar= int(input("Escriba el ID del estudiante que desea eliminar: "))
                BD.pop(id_eliminar)
                
                print("Estudiante eliminado exitosamente! \n")
                
            elif opcionestu=='5':
                print("Volviendo al Menu Principal")
                break
            
            else:
                print("Dato inválido, escribe otro: ")
                