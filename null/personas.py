class personas:

    def Menu():
            BD = {}

            while True:
                print("\n----------Menu personas----------")
                print("1. crear")
                print("2. listar")
                print("3. actualizar")
                print("4. eliminar")
                print("5. volver al menu principal")

                seleccion = input("escoja una opcion: ")

                if seleccion=='1':
                    print("-----Crear-----")
                    id= int(input("escriba el ID: "))
                    nombre= input("escriba el nombre: ")
                    apellido= input("escriba el apellido: ")
                    edad= input("escriba el edad: ")
                    
                    if id in BD:
                        print("Ya existe un usuario con esa ID")
                        continue 
                    else:
                        BD[id]=[nombre,apellido,edad]
                        print("¡datos guardados!")    

                elif seleccion=='2':
                    
                    print("-----Lista-----")
                    for id_persona, datos in BD.items():
                        print("ID:", id_persona)
                        print("Nombre:", datos[0],datos[1])
                        print("Edad:", datos[2],"\n")
                
                elif seleccion=='3':
                    print("-----Actualizar-----")
                    id_buscar= int(input("escriba el ID que desea modificar: "))
                    nombre_mod= input("escriba el nombre: ")
                    apellido_mod= input("escriba el apellido: ")
                    edad_mod= input("escriba el edad: ")

                    BD[id_buscar][0]=nombre_mod
                    BD[id_buscar][1]=apellido_mod
                    BD[id_buscar][2]=edad_mod

                    print("¡Datos modificados exitosamente!")
                    print(BD[id_buscar])

                elif seleccion=='4':
                    print("-----Eliminar-----")
                    id_del= int(input("escriba el ID que desea eliminar: "))
                    BD.pop(id_del)
                    print("¡Dato eliminado exitosamente!")
                
                elif seleccion=='5':
                    print("-----Volviendo al Menú principal-----")
                    break
                
                else:
                    print("Elige un dato válido")
                    
