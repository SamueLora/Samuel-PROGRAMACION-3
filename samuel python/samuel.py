class Person:
  def __init__(self, nombre="Samuel", apellido="Lora", correo="samuelora0410@gmail.com", telefono= "3022336125"):
    self.nombre = nombre
    self.apellido = apellido
    self.correo = correo
    self.telefono = telefono

  def Obtenerinfo(self):
    
    print("Mi nombre es", self.nombre, self.apellido,"mi correo es:", self.correo, ", y mi numero telefónico es", self.telefono)