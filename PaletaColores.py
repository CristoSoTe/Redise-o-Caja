import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Abrir el selector de color
color = colorchooser.askcolor()

# Imprimir el color seleccionado
if color[1] is not None:
    print("Color seleccionado:", color[1])

root.destroy()