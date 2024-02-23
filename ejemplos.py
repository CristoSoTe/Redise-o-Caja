import tkinter as tk

class MiApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.frame_botones = tk.Frame(self)
        self.frame_botones.pack()

        # self.photoSube = tk.PhotoImage(file="path_to_your_image")
        # self.photoBaja = tk.PhotoImage(file="path_to_your_image")

        self.lista_etiquetas_series_preparadas = []

        for i in range(1, 10):
            color = "white"
            etiqueta_rotulo_titulo = tk.Label(self.frame_botones, text=f"RANGO {i}", bg=color, font=("Times New Roman", 15, "bold"))
            etiqueta_rotulo_titulo.pack(padx=10, pady=10)
            etiqueta_rotulo_series = tk.Label(self.frame_botones, text="SERIES", bg=color, font=("Arial", 10, "bold"))
            etiqueta_rotulo_series.pack(padx=10, pady=10)
            etiqueta_series = tk.Label(self.frame_botones, text="0", fg="blue", bg="white", font=("Times New Roman", 17, "bold"))
            etiqueta_series.pack(padx=10, pady=10)
            self.lista_etiquetas_series_preparadas.append(etiqueta_series)
            colores_botones = ["blue", "#8B0000", "blue"]
            indice = 0

            for j in range(3):
                if j == 0:
                    boton = tk.Button(self.frame_botones, text=f"SUBIR", bg=colores_botones[indice], command=lambda i=i, j=j: self.on_click(i, j))
                elif j == 1:
                    boton = tk.Button(self.frame_botones, text=f"SUBIR", bg=colores_botones[indice], fg="white", command=lambda i=i, j=j: self.on_click(i, j))
                else:
                    boton = tk.Button(self.frame_botones, text=f"SUBIR", bg=colores_botones[indice], command=lambda i=i, j=j: self.on_click(i, j))
                
                boton.pack(pady=4)
                indice += 1

        # Agregar botón "Salir"
        boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.salir)
        boton_salir.pack(pady=4)

    def on_click(self, i, j):
        # Comportamiento específico de cada botón
        
        print(f"Botón presionado en RANGO {i}, posición {j}")

    def salir(self):
        self.destroy()  # Cierra la ventana de la aplicación

if __name__ == "__main__":
    app = MiApp()
    app.mainloop()