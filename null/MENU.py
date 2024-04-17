from personas import personas

def MenuPrincipal():
    while True:
       print("----------Menu principal----------")
       print("1. personas")
       print("2. salir")

       opcion = input("escoja una opcion: ")

       if opcion=='1':
           p= personas
           print(p.Menu())
       elif opcion=='2':
           print("Chao")
           break
       else:
           print("Elije una opcion válida")


MenuPrincipal()