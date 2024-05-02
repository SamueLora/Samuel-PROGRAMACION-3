import tkinter as tk


def mostrar_datos():
    nuevo_frame = tk.Frame(ventana, padx=10, pady=10)
    nuevo_frame.grid(row=6, column=0, columnspan=3)
    nuevo_frame.config(borderwidth=2, relief="solid")
    
    
    
    nombre = text_nombre.get()
    apellido = text_apellido.get()
    edad = text_edad.get()
    sexo = "Masculino" if opcion.get() == 1 else "Femenino"
    ciudad = rciudad.get(rciudad.curselection())

    tk.Label(nuevo_frame, text="Nombre: " + nombre).grid(row=0, column=0, sticky="w")
    tk.Label(nuevo_frame, text="Apellido: " + apellido).grid(row=1, column=0, sticky="w")
    tk.Label(nuevo_frame, text="Edad: " + edad).grid(row=2, column=0, sticky="w")
    tk.Label(nuevo_frame, text="Sexo: " + sexo).grid(row=3, column=0, sticky="w")
    tk.Label(nuevo_frame, text="Ciudad: " + ciudad).grid(row=4, column=0, sticky="w")

ventana = tk.Tk()
ventana.title("Registro Samuel :)")
ventana.geometry("500x800")

nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.grid(row=0, column=0)
text_nombre = tk.Entry(ventana, width=30)
text_nombre.grid(row=0, column=1)

apellido_label = tk.Label(ventana, text="Apellido:")
apellido_label.grid(row=1, column=0)
text_apellido = tk.Entry(ventana, width=30)
text_apellido.grid(row=1, column=1)

edad_label = tk.Label(ventana, text="Edad:")
edad_label.grid(row=2, column=0)
text_edad = tk.Entry(ventana, width=30)
text_edad.grid(row=2, column=1)

sexo_label = tk.Label(ventana, text="Sexo:")
sexo_label.grid(row=3, column=0)
opcion = tk.IntVar()
rsexo_M = tk.Radiobutton(ventana, text="Masculino", variable=opcion, value=1)
rsexo_M.grid(row=3, column=1)
rsexo_F = tk.Radiobutton(ventana, text="Femenino", variable=opcion, value=2)
rsexo_F.grid(row=3, column=2)

ciudad_label = tk.Label(ventana, text="Ciudad:")
ciudad_label.grid(row=4, column=0)
rciudad = tk.Listbox(ventana, width=30)
elementos = ["Cartagena", "Medellín", "Cúcuta", "Barranquilla", "Bogotá", "Santa Marta"]
for elemento in elementos:
    rciudad.insert(tk.END, elemento)
rciudad.grid(row=4, column=1)

boton = tk.Button(ventana, text="Registrar", command=mostrar_datos)
boton.grid(row=5, column=1, padx=10, pady=10)

ventana.mainloop()
