import tkinter as tk

ventana = tk.Tk()

ventana.title("Registro de Usuarios")
ventana.geometry("500x800")

nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=10, pady=5)
text_nombre = tk.Entry(ventana, width=30)
text_nombre.grid(row=0, column=1, padx=10, pady=5)

apellido_label = tk.Label(ventana, text="Apellido:")
apellido_label.grid(row=1, column=0, padx=10, pady=5)
text_apellido = tk.Entry(ventana, width=30)
text_apellido.grid(row=1, column=1, padx=10, pady=5)

edad_label = tk.Label(ventana, text="Edad:")
edad_label.grid(row=2, column=0, padx=10, pady=5)
text_edad = tk.Entry(ventana, width=30)
text_edad.grid(row=2, column=1, padx=10, pady=5)

sexo_label = tk.Label(ventana, text="Sexo:")
sexo_label.grid(row=3, column=0, padx=10, pady=5)
rsexo_M = tk.Radiobutton(ventana, text="Masculino", variable="opcion", value=1)
rsexo_M.grid(row=3, column=1, padx=10, pady=5)
rsexo_F = tk.Radiobutton(ventana, text="Femenino", variable="opcion", value=2)
rsexo_F.grid(row=3, column=2, padx=10, pady=5)

ciudad_label = tk.Label(ventana, text="Ciudad:")
ciudad_label.grid(row=4, column=0, padx=10, pady=5)
rciudad = tk.Listbox(ventana, width=30)
elementos = ["Cartagena", "Bogotá", "Barranquilla"]
for elemento in elementos:
    rciudad.insert(tk.END, elemento)
rciudad.grid(row=4, column=1, padx=10, pady=5)

boton = tk.Button(ventana, text="Registrar")
boton.grid(row=5, column=1, padx=10, pady=10)

ventana.mainloop()
