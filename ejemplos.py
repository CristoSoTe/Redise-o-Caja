import tkinter as tk

# Crear la ventana
root = tk.Tk()

# Definir los textos
variable1_text = "Variable1"
variable2_text = "Variable2"

# Crear el widget de texto
text_widget = tk.Text(root)
text_widget.pack()

# Insertar texto con diferentes fuentes
text_widget.insert("end", variable1_text, "font_variable1")
text_widget.insert("end", "-", "normal")
text_widget.insert("end", variable2_text, "font_variable2")

# Configurar las fuentes
text_widget.tag_configure("font_variable1", font=("Arial", 12))
text_widget.tag_configure("font_variable2", font=("Arial", 8))

# Deshabilitar la edición del widget de texto
text_widget.config(state="disabled")

root.mainloop()