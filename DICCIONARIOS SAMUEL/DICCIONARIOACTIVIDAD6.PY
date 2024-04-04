#1
print("#1")
Perro={}
print(Perro)
print( )

#2
print("#2")
Perro['nombre']= 'Roberto'
Perro['color']= 'Marrón'
Perro['raza']= 'Rottweiler'
Perro['patas']= '4'
Perro['edad']= '10 meses'
print(Perro)
print( )

#3
print("#3")
Estudiante={'nombre': 'Samuel', 'apellido': 'Lora', 'sexo': 'Masculino', 'edad': '19', 'estado_civil': 'Soltero', 'habilidades': ['Programador'], 'pais': 'Colombia', 'ciudad': 'Cartagena', 'direccion': 'Mi casa, cra Micasa123'}
print(Estudiante)
print( )

#4
print("#4")
print(Estudiante.__len__())
print( )

#5
print("#5")
print(Estudiante['habilidades'])
print(type(Estudiante['habilidades']))
print( )

#6
print("#6")
Estudiante['habilidades'].append('Bilingue')
print(Estudiante)
print( )

#7
print("#7")
lista= Estudiante.keys()
print(lista)
print( )

#8
print("#8")
lista2= Estudiante.values()
print(lista2)
print( )

#9
print("#9")
lista3= Estudiante.items()
print(lista3)
print( )

#10
print("#10")
Estudiante.popitem()
print(Estudiante)
print( )

#11
print("#11")
del Estudiante
print( )