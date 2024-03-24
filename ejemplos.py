import tkinter as tk

def copiar_valores():
    for label_origen, label_destino in zip(lista_labels_origen, lista_labels_destino):
        texto_origen = label_origen.cget("text")
        label_destino.config(text=texto_origen)

# Crear la ventana principal
root = tk.Tk()
root.geometry("400x200")
root.title("Copiar valores entre listas de Label")

# Definir las listas de Labels
lista_labels_origen = [tk.Label(root, text=f"Texto {i+1}") for i in range(5)]
lista_labels_destino = [tk.Label(root, text="") for _ in range(5)]

# Posicionar los Labels en la ventana
for label in lista_labels_origen:
    label.pack(side=tk.LEFT, padx=10)

for label in lista_labels_destino:
    label.pack(side=tk.RIGHT, padx=10)

# Crear un botón para copiar los valores entre las listas
boton_copiar = tk.Button(root, text="Copiar Valores", command=copiar_valores)
boton_copiar.pack(pady=10)

root.mainloop()