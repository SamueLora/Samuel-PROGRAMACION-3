import tkinter as tk

def abrir_ventana_home():
    ventana_home = tk.Toplevel()
    ventana_home.title("Home")
    tk.Label(ventana_home, text="Home").pack()

def datosusuario():
    usuario = entry_usuario.get()
    clave = entry_contraseña.get()
    
    if usuario == "luz karime" and clave == "12345":
        app.destroy()  # Cerrar la ventana actual
        abrir_ventana_home()  # Abrir una nueva ventana con el texto "home"
    
app = tk.Tk()
app.title("Login Colegio")
app.geometry("800x400")
# Cargar el logo
logo = tk.PhotoImage(file="C:/Users/Biblioteca/Desktop/SAMUEL LOGIN1/logo.png")


frame_logo = tk.Frame(app)
frame_logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

frame_contenido = tk.Frame(app)
frame_contenido.grid(row=0, column=1, padx=10, pady=10)


label_logo = tk.Label(frame_logo, image=logo)
label_logo.pack(padx=100, pady=100)


tk.Label(frame_contenido, text="Usuario", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=110, pady=5, sticky="e")
entry_usuario = tk.Entry(frame_contenido, width="35")
entry_usuario.grid(row=1, column=0, padx=10, pady=5)

tk.Label(frame_contenido, text="Contraseña", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=100, pady=5, sticky="e")
entry_contraseña = tk.Entry(frame_contenido, show="•", width="35")
entry_contraseña.grid(row=3, column=0, padx=10, pady=5)
entry_usuario.focus()

boton= tk.Button(frame_contenido, text="Inicio", width="30", command=datosusuario)
boton.grid(row=4, column=0, padx=10, pady=30)

app.resizable(False, False)




app.mainloop()