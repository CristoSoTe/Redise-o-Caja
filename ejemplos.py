import tkinter as tk
from tkinter import colorchooser

<<<<<<< HEAD
def choose_color():
    color = colorchooser.askcolor(title="Elige un color")
    if color[1]:  # Verifica si se seleccionó un color
        color_code = color[1]  # Obtiene el código del color en hexadecimal
        print("Color seleccionado:", color_code)  # Imprime el código del color

root = tk.Tk()
root.title("Paleta de colores de Windows")

button = tk.Button(root, text="Abrir Paleta de Colores", command=choose_color)
button.pack(pady=20)

=======
# Crear la ventana principal
root = tk.Tk()

# Crear un botón con el color de fondo verde
boton_verde = tk.Button(root, text="Botón verde", highlightbackground="green")
boton_verde.pack()

# Ejecutar el bucle principal
>>>>>>> 8ee3d3fa09791eeb62a657844fb27c3a404924fc
root.mainloop()