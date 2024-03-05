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

        self.ventana.grid_rowconfigure(0, weight=1)
        for i in range(10):
            self.ventana.grid_columnconfigure(i, weight=1)

        colores = ["gray59", "#C0C0C0"]
        # Etiquetas en la parte superior
        self.etiquetas_venta = []
        for i in range(10):
            color = colores[i % 2]  # Alternar entre los dos colores
            frame_venta = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            frame_venta.grid(row=0, column=i, sticky="nsew")  # sticky para expandir la columna
            etiqueta = tk.Label(frame_venta, text="0", bg="white")
            etiqueta.pack(padx=10, pady=10)
            self.etiquetas_venta.append(etiqueta)

        
        self.lista_etiquetas_titulos = []
        self.lista_etiquetas_series_venta = []
        for i in range(10):
            color = colores[i % 2]  # Alternar entre los dos colores
            frame_inferior = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            frame_inferior.grid(row=1, column=i, sticky="nsew")  # sticky para expandir la columna
            etiqueta_rotulo_titulo = tk.Label(frame_inferior, text=f"RANGO {i+1}", bg="white")
            etiqueta_rotulo_titulo.pack(padx=10, pady=10)
            etiqueta_series = tk.Label(frame_inferior, text="0", bg="white")
            etiqueta_series.pack(padx=10, pady=10)
            self.lista_etiquetas_titulos.append(etiqueta_rotulo_titulo)
            self.lista_etiquetas_series_venta.append(etiqueta_series)



        # #Frame botoes (fondo verde)
        # frame_botones = tk.Frame(self.ventana, bg="green")
        # frame_botones.grid(row=2)#pack(fill="both", expand=True)

        # # Botones divididos en tres filas
        # for i in range(27):
        #     fila = i // 9
        #     columna = i % 9
        #     boton = tk.Button(frame_botones, text=f"Botón {i+1}")
        #     boton.grid(row=fila + 2, column=columna, padx=5, pady=5)

        self.lista_etiquetas_series_preparadas = []
        for i in range(11):
            color = colores[i % 2]  # Alternar entre los dos colores
            frame_botones = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            frame_botones.grid(row=2, column=i, sticky="nsew")  # sticky para expandir la columna
            if i == 0:
                rotulos = ["HISTÓRICO", "RESET", "SALIR"]
                colores_botones = ["Green", "#8B0000", "red"]
                indice = 0
                for j in range(3):
                    boton = tk.Button(frame_botones, text=rotulos[indice], fg = "white", bg = colores_botones[indice], width=10, height=2,font=("Times New Roman",15,"bold"),cursor="hand2")
                    boton.pack(pady = 10)
                    indice += 1
                    if j == 2:
                        boton.config(command=lambda: cerrar_programa(self.ventana))
            
            elif i > 0 and i < 10:
                etiqueta_rotulo_titulo = tk.Label(frame_botones, text=f"RANGO {i}", bg=color, font=("Times New Roman",15,"bold"))
                etiqueta_rotulo_titulo.pack(padx=10, pady=10)
                etiqueta_rotulo_series = tk.Label(frame_botones, text="SERIES", bg=color, font=("Arial",10,"bold"))
                etiqueta_rotulo_series.pack(padx=10, pady=10)
                etiqueta_series = tk.Label(frame_botones, text="0", fg="blue", bg = "white", font=("Times New Roman",17,"bold"))
                etiqueta_series.pack(padx=10, pady=10)
                self.lista_etiquetas_series_preparadas.append(etiqueta_series)
                colores_botones = ["blue", "#8B0000", "blue"]
                indice = 0

                for j in range(3):
                    if j == 0:
                        boton = tk.Button(frame_botones, text=f"SUBIR", bg=colores_botones[indice], command=lambda i=i, j=j: self.on_click(i, j))
                    elif j == 1:
                        boton = tk.Button(frame_botones, text=f"SUBIR", bg=colores_botones[indice], fg="white", command=lambda i=i, j=j: self.on_click(i, j))
                    else:
                        boton = tk.Button(frame_botones, text=f"SUBIR", bg=colores_botones[indice], command=lambda i=i, j=j: self.on_click(i, j))
                    
                    boton.pack(pady=4)
                    indice += 1

                    # if j == 0:
                    #     boton.config(command=lambda: incrementar_etiqueta(self.lista_etiquetas_series_preparadas[0]))
                    # if j == 1:
                    #     boton.config(command=lambda: subir_a_venta(self.lista_etiquetas_series_preparadas[0], self.lista_etiquetas_series_venta[0]))
                    # if j == 2:
                    #     boton.config(command=lambda: restar_etiqueta(self.lista_etiquetas_series_preparadas[0]))
            else:
                boton = tk.Button(frame_botones, text="COMENZAR", width=10, height=2, bg="green", fg="white",font=("Times New Roman",15,"bold"),cursor="hand2")
                boton.pack(padx=5, pady=100)

    def on_click(self, i, j):
        # Comportamiento específico de cada botón
        if i == 1 and j == 0:
            incrementar_etiqueta(self.lista_etiquetas_series_preparadas[0])
        elif i == 1 and j == 1:
            subir_a_venta(self.lista_etiquetas_series_preparadas[0], self.lista_etiquetas_series_venta[0])
        elif i == 1 and j == 2:
            restar_etiqueta(self.lista_etiquetas_series_preparadas[0])
        elif i == 2 and j == 0:
            incrementar_etiqueta(self.lista_etiquetas_series_preparadas[1])
        elif i == 2 and j == 1:
            subir_a_venta(self.lista_etiquetas_series_preparadas[1], self.lista_etiquetas_series_venta[1])
        elif i == 2 and j == 2:
            restar_etiqueta(self.lista_etiquetas_series_preparadas[1])
        elif i == 3 and j == 0:
            incrementar_etiqueta(self.lista_etiquetas_series_preparadas[2])
        elif i == 3 and j == 1:
            subir_a_venta(self.lista_etiquetas_series_preparadas[2], self.lista_etiquetas_series_venta[2])
        elif i == 3 and j == 2:
            restar_etiqueta(self.lista_etiquetas_series_preparadas[2])


        
        print(f"Botón presionado en RANGO {i}, posición {j}")


    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    mi_ventana = Ventana()
    mi_ventana.ejecutar()