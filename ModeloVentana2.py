import tkinter as tk
from funciones import *

class Ventana():
    def __init__(self):
        #super().__init__()

        self.ventana = tk.Tk()
        self.ventana.title("Ventana con Etiquetas y Botones")
        self.ventana.geometry("1600x900")
        #self.ventana.attributes('-fullscreen', True)

        self.photoSube=tk.PhotoImage(file=r"C:\Users\crist\OneDrive\Escritorio\CajaCopilot\flechaSube.png")
        self.photoBaja=tk.PhotoImage(file=r"C:\Users\crist\OneDrive\Escritorio\CajaCopilot\flechaBaja.png")

        #self.ventana.grid_rowconfigure(0, weight=1)
        for i in range(11):
            self.ventana.grid_columnconfigure(i, weight=1)

        self.frame_columna4 = tk.Frame(self.ventana, bg="blue", bd=2, relief="groove")
        self.frame_columna4.grid(row=0, column=0, columnspan=11, sticky="nsew")
        self.etiqueta_zona_venta = tk.Label(self.frame_columna4, text=f"LIQUIDACIÓN", font=("Times New Roman",18,"bold"), bg="blue", fg="white" ) # Etiqueta numero de rango en liquidacion
        self.etiqueta_zona_venta.pack(pady=5)

        # LISTAS
        self.lista_liquidacion_euros = []
        self.lista_numero_series_liquidacion = []
        self.lista_cartones_liquidacion = []

        colores = ["gray59", "#C0C0C0"]
        for i in range(11):
            color = colores[i % 2]  # Alternar entre los dos colores

            self.frame_columna = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            self.frame_columna.grid(row=1, column=i, sticky="nsew")  # sticky para expandir la columna

            # if i == 0:
            #     self.frame_columna.config(bg="#87CEEB")
            #     etiqueta = tk.Label(self.frame_columna, text="PRECIOS", bg="white", font=("Times New Roman",15,"bold"))
            #     etiqueta.pack(padx=10, pady=10)
            #     indice = 0
            #     for j in range (4):
            #         precios = ["1,5", "2", "3", "6"]
            #         etiqueta = tk.Label(self.frame_columna, text=precios[indice], bg="white")
            #         etiqueta.pack(padx=10, pady=10)
            #         indice += 1

            #     linea_divisoria(self.frame_columna)

            if i == 0:
                # COLUMNA RANGO 1
                self.frame_columna.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_rango1 = tk.Label(self.frame_columna, text=f"RANGO 1", font=("Times New Roman",18,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rango1.pack(padx=10, pady=10)

                self.euros_liquidacion_rango1 = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_rango1.pack()
                self.lista_liquidacion_euros.append(self.euros_liquidacion_rango1)

                self.etiqueta_series_liquidacion_rango1=tk.Label(self.frame_columna, text = "SERIES + Pico", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_series_liquidacion_rango1.pack()

                self.numero_series_liquidacion_rango1 = tk.Label(self.frame_columna, text="0", fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
                self.numero_series_liquidacion_rango1.pack()
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_rango1)

                self.etiqueta_del_al_liquidacion_rango1=tk.Label(self.frame_columna, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_del_al_liquidacion_rango1.pack()

                self.cartones_liquidacion_rango1 = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_rango1.pack()
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_rango1)

                #linea_divisoria(self.frame_columna) 

            if i > 0 and i < 9:
                # COLUMNA RANGOS DEL 2 AL 9
                self.etiqueta_rotulo_titulo_rangos = tk.Label(self.frame_columna, text=f"RANGO {i}", bg=color, font=("Times New Roman",18,"bold")) # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rangos.pack(padx=10, pady=10)

                self.euros_liquidacion_rangos = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_rangos.pack()
                self.lista_liquidacion_euros.append(self.euros_liquidacion_rangos)

                self.etiqueta_series_liquidacion_rangos=tk.Label(self.frame_columna, text = "SERIES", font=("Times New Roman", 13,"bold"), bg=color)
                self.etiqueta_series_liquidacion_rangos.pack()

                self.numero_series_liquidacion_rangos = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.numero_series_liquidacion_rangos.pack()
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_rangos)

                self.etiqueta_del_al_liquidacion_rangos=tk.Label(self.frame_columna, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg=color)
                self.etiqueta_del_al_liquidacion_rangos.pack()

                self.cartones_liquidacion_rangos = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_rangos.pack()
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_rangos)

            if i == 9:
                #COLUMNA RANGO CIERRE
                self.frame_columna.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_cierre = tk.Label(self.frame_columna, text=f"CIERRE", font=("Times New Roman",18,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_cierre.pack(padx=10, pady=10)

                self.euros_liquidacion_cierre = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_cierre.pack()
                self.lista_liquidacion_euros.append(self.euros_liquidacion_cierre)

                self.etiqueta_series_liquidacion_rangos=tk.Label(self.frame_columna, text = "SERIES + Pico", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_series_liquidacion_rangos.pack()

                self.numero_series_liquidacion_cierre = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
                self.numero_series_liquidacion_cierre.pack()
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_cierre)

                self.etiqueta_del_al_liquidacion_cierre=tk.Label(self.frame_columna, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_del_al_liquidacion_cierre.pack()

                self.cartones_liquidacion_cierre = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_cierre.pack()
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_cierre)

            if i == 10:
                # COLUMNA TOTAL
                self.frame_columna.config(bg="#0099ff")
                etiqueta_rotulo_titulo_total = tk.Label(self.frame_columna, text=f"TOTAL", bg="#0099ff", font=("Times New Roman",18,"bold")) # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo_total.pack(padx=10, pady=10)

                self.euros_liquidacion_total = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_total.pack()
                self.lista_liquidacion_euros.append(self.euros_liquidacion_total)

                etiqueta_liquidacion_total=tk.Label(self.frame_columna, text = "SERIES", font=("Times New Roman", 13,"bold"), bg="#0099ff")
                etiqueta_liquidacion_total.pack()

                self.numero_series_liquidacion_total = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.numero_series_liquidacion_total.pack()
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_total)

                self.etiqueta_del_al_liquidacion_total=tk.Label(self.frame_columna, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg="#0099ff")
                self.etiqueta_del_al_liquidacion_total.pack()

                self.cartones_liquidacion_total = tk.Label(self.frame_columna, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_total.pack()
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_total)


        self.frame_columna2 = tk.Frame(self.ventana, bg="blue", bd=2, relief="groove")
        self.frame_columna2.grid(row=2, column=0, columnspan=11, sticky="nsew")
        self.etiqueta_zona_venta = tk.Label(self.frame_columna2, text=f"VENTA", font=("Times New Roman",18,"bold"), bg="blue", fg="white" ) # Etiqueta numero de rango en liquidacion
        self.etiqueta_zona_venta.pack(pady=5)

        for i in range(11):
            color = colores[i % 2]  # Alternar entre los dos colores

            self.frame_columna3 = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            self.frame_columna3.grid(row=3, column=i, sticky="nsew")

            if i == 0:
                # COLUMNA RANGO 1
                self.frame_columna3.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_rango1 = tk.Label(self.frame_columna3, text=f"SERIES", font=("Times New Roman",13,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rango1.pack(padx=10, pady=10)

            if i > 0 and i < 9:
                # COLUMNA RANGOS DEL 2 AL 9
                self.etiqueta_rotulo_titulo_rangos = tk.Label(self.frame_columna3, text=f"SERIES", bg=color, font=("Times New Roman",13,"bold")) # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rangos.pack(padx=10, pady=10)

            if i == 9:
                #COLUMNA RANGO CIERRE
                self.frame_columna3.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_cierre = tk.Label(self.frame_columna3, text=f"SERIES", font=("Times New Roman",13,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_cierre.pack(padx=10, pady=10)

            if i == 10:
                # COLUMNA TOTAL
                self.frame_columna3.config(bg="#0099ff")
                etiqueta_rotulo_titulo_total = tk.Label(self.frame_columna3, text=f"PRECIOS", bg="#0099ff", font=("Times New Roman",13,"bold")) # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo_total.pack(padx=10, pady=10)






    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    mi_ventana = Ventana()
    mi_ventana.ejecutar()
