import tkinter as tk
from funciones import *

class Ventana():
    def __init__(self):
        #super().__init__()

        self.ventana = tk.Tk()
        self.ventana.title("Ventana con Etiquetas y Botones")
        self.ventana.geometry("1600x900")

        self.photoSube=tk.PhotoImage(file=r"C:\Users\crist\OneDrive\Escritorio\CajaCopilot\flechaSube.png")
        self.photoBaja=tk.PhotoImage(file=r"C:\Users\crist\OneDrive\Escritorio\CajaCopilot\flechaBaja.png")

        #self.ventana.grid_rowconfigure(0, weight=1)
        for i in range(12):
            self.ventana.grid_columnconfigure(i, weight=1)

        colores = ["gray59", "#C0C0C0"]
        # Etiquetas en la parte superior
        self.etiquetas_venta = []
        for i in range(12):
            color = colores[i % 2]  # Alternar entre los dos colores

            frame_columna = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            frame_columna.grid(row=0, column=i, sticky="nsew")  # sticky para expandir la columna

            if i == 0:
                frame_columna.config(bg="#87CEEB")
                indice = 0
                for j in range (4):
                    precios = ["1,5", "2", "3", "6"]
                    etiqueta = tk.Label(frame_columna, text=precios[indice], bg="white")
                    etiqueta.pack(padx=10, pady=10)
                    indice += 1

            if i == 1:
                etiqueta_rotulo_titulo = tk.Label(frame_columna, text=f"RANGO 1", bg="white") # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo.pack(padx=10, pady=10) 

            if i > 1 and i < 10:
                etiqueta_rotulo_titulo = tk.Label(frame_columna, text=f"RANGO {i}", bg="white") # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo.pack(padx=10, pady=10)

            if i == 10:
                etiqueta_rotulo_titulo = tk.Label(frame_columna, text=f"CIERRE", bg="white") # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo.pack(padx=10, pady=10)
            if i == 11:
                etiqueta_rotulo_titulo = tk.Label(frame_columna, text=f"TOTAL", bg="white") # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo.pack(padx=10, pady=10)

    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    mi_ventana = Ventana()
    mi_ventana.ejecutar()
