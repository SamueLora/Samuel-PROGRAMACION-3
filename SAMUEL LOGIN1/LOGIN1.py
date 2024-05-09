import tkinter as tk

# Crear la app principal
app = tk.Tk()
app.title("Login Colegio")

# Cargar el logo
logo = tk.PhotoImage(file="C:/Users/Biblioteca/Desktop/SAMUEL LOGIN1/logo.png")

# Crear un Frame para el logo y otro para el contenido
frame_logo = tk.Frame(app)
frame_logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

frame_contenido = tk.Frame(app)
frame_contenido.grid(row=0, column=1, padx=10, pady=10)

# Mostrar el logo en el Frame correspondiente
label_logo = tk.Label(frame_logo, image=logo)
label_logo.pack(padx=10, pady=10)

# Crear widgets para usuario y contraseña en el Frame de contenido
tk.Label(frame_contenido, text="Usuario:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_usuario = tk.Entry(frame_contenido)
entry_usuario.grid(row=0, column=1, padx=10, pady=5, sticky="w")  # Centrar el entry con respecto al label

tk.Label(frame_contenido, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_contraseña = tk.Entry(frame_contenido, show="•")
entry_contraseña.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # Centrar el entry con respecto al label

# Ejecutar el bucle principal de la aplicación
app.mainloop()
