import tkinter as tk
from funciones import *

#NO FUNCIONAN LOS BOTONES

class Ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana con Etiquetas y Botones")
        self.ventana.geometry("1600x900")

        colores = ["red", "blue"]
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
        self.lista_etiquetas_series = []
        for i in range(10):
            color = colores[i % 2]  # Alternar entre los dos colores
            frame_inferior = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            frame_inferior.grid(row=1, column=i, sticky="nsew")  # sticky para expandir la columna
            etiqueta_titulo = tk.Label(frame_inferior, text=f"RANGO {i+1}", bg="white")
            etiqueta_titulo.pack(padx=10, pady=10)
            etiqueta_series = tk.Label(frame_inferior, text="0", bg="white")
            etiqueta_series.pack(padx=10, pady=10)
            self.lista_etiquetas_titulos.append(etiqueta_titulo)
            self.lista_etiquetas_series.append(etiqueta_series)



        # #Frame botoes (fondo verde)
        # frame_botones = tk.Frame(self.ventana, bg="green")
        # frame_botones.grid(row=2)#pack(fill="both", expand=True)

        # # Botones divididos en tres filas
        # for i in range(27):
        #     fila = i // 9
        #     columna = i % 9
        #     boton = tk.Button(frame_botones, text=f"Botón {i+1}")
        #     boton.grid(row=fila + 2, column=columna, padx=5, pady=5)

        for i in range(10):
            color = colores[i % 2]  # Alternar entre los dos colores
            frame_botones = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            frame_botones.grid(row=2, column=i, sticky="nsew")  # sticky para expandir la columna
            contador_boton = 0
            for j in range(3):
                boton = tk.Button(frame_botones, text=f"Botón {j+1}")
                boton.pack()
                contador_boton += 1

                if contador_boton == 0:
                    boton.config(command=lambda: incrementar_etiqueta(self.lista_etiquetas_series[0]))
                if contador_boton == 1:
                    boton.config(command=lambda: incrementar_etiqueta(self.lista_etiquetas_series[0]))
                if contador_boton == 2:
                    boton.config(command=lambda: restar_etiqueta(self.lista_etiquetas_series[0]))

            # # Asociar la función sumar a los botones sumar 1
            # if i == 0:
            #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[0]))
            # if i == 1:
            #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[1]))
            # if i == 2:
            #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[2]))
            # if i == 3:
            #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[3]))
            # if i == 4:
            #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[4]))
            # if i == 5:
            #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[5]))
            # if i == 6:
            #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[6]))
            # if i == 7:
            #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[7]))
            # if i == 8:
            #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[8]))
            # # if i == 9:
            # #     boton.config(command=lambda: incrementar_etiqueta(self.etiquetas_inferiores[9]))

            # # Asociar la función restar a los botones restar 1
            # if i == 18:
            #     boton.config(command=lambda: restar_etiqueta(self.etiquetas_inferiores[0]))
            # if i == 19:
            #     boton.config(command=lambda: restar_etiqueta(self.etiquetas_inferiores[1]))
            # if i == 20:
            #     boton.config(command=lambda: restar_etiqueta(self.etiquetas_inferiores[2]))
            # if i == 21:
            #     boton.config(command=lambda: restar_etiqueta(self.etiquetas_inferiores[3]))
            # if i == 22:
            #     boton.config(command=lambda: restar_etiqueta(self.etiquetas_inferiores[4]))
            # if i == 23:
            #     boton.config(command=lambda: restar_etiqueta(self.etiquetas_inferiores[5]))
            # if i == 24:
            #     boton.config(command=lambda: restar_etiqueta(self.etiquetas_inferiores[6]))
            # if i == 25:
            #     boton.config(command=lambda: restar_etiqueta(self.etiquetas_inferiores[7]))
            # if i == 26:
            #     boton.config(command=lambda: restar_etiqueta(self.etiquetas_inferiores[8]))

    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    mi_ventana = Ventana()
    mi_ventana.ejecutar()