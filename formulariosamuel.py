import tkinter as tk

def registrar():
    print("Nombre:", textnombre.get())
    print("Apellido:", textapellido.get())
    print("Edad:", textedad.get())
    if opcion.get() == 1:
        print("Sexo: Male")
    elif opcion.get() == 2:
        print("Sexo: Female")
    print("Ciudad:", rciudad.get(rciudad.curselection()))

ventana = tk.Tk()
ventana.title("Registro de Usuario")
ventana.geometry("400x300")

titulo = tk.Label(ventana, text="Formulario de Registro", font=("Helvetica", 16))
titulo.pack(pady=10)

frame_datos = tk.Frame(ventana)
frame_datos.pack(pady=10)

tk.Label(frame_datos, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
textnombre = tk.Entry(frame_datos, width=20)
textnombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_datos, text="Apellido:").grid(row=1, column=0, padx=5, pady=5)
textapellido = tk.Entry(frame_datos, width=20)
textapellido.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_datos, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
textedad = tk.Entry(frame_datos, width=20)
textedad.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_datos, text="Sexo:").grid(row=3, column=0, padx=5, pady=5)
opcion = tk.IntVar()
tk.Radiobutton(frame_datos, text="Masculino", variable=opcion, value=1).grid(row=3, column=1, padx=5, pady=5)
tk.Radiobutton(frame_datos, text="Femenino", variable=opcion, value=2).grid(row=3, column=2, padx=5, pady=5)

tk.Label(frame_datos, text="Ciudad:").grid(row=4, column=0, padx=5, pady=5)
rciudad = tk.Listbox(frame_datos, width=20, selectmode="SINGLE")
elementos = ["Cartagena", "Bogota   ", "Barranquilla"]
for elemento in elementos:
    rciudad.insert(tk.END, elemento)
rciudad.grid(row=4, column=1, padx=5, pady=5)

boton = tk.Button(ventana, text="Registrar", command=registrar, bg="blue", fg="white", width=10)
boton.pack(pady=10)

ventana.mainloop()
