import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color = colorchooser.askcolor(title="Elige un color")
    if color[1]:  # Verifica si se seleccionó un color
        color_code = color[1]  # Obtiene el código del color en hexadecimal
        print("Color seleccionado:", color_code)  # Imprime el código del color

root = tk.Tk()
root.title("Paleta de colores de Windows")

button = tk.Button(root, text="Abrir Paleta de Colores", command=choose_color)
button.pack(pady=20)

root.mainloop()