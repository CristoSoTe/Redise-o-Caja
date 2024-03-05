import tkinter as tk
from funciones import *
import os

class Ventana():
    def __init__(self):
        #super().__init__()

        self.ventana = tk.Tk()
        self.ventana.attributes('-fullscreen', True)

        # self.ventana.title("Ventana con Etiquetas y Botones")
        #self.ventana.geometry("1600x900")

        self.photoSube=tk.PhotoImage(file=r"C:\Users\crist\OneDrive\Escritorio\CajaCopilot\flechaSube.png")
        self.photoBaja=tk.PhotoImage(file=r"C:\Users\crist\OneDrive\Escritorio\CajaCopilot\flechaBaja.png")

        #---CONFIGURACION DE LAS COLUMNAS
        for i in range(7):
            self.ventana.grid_rowconfigure(i, weight=1)
        for i in range(11):
            self.ventana.grid_columnconfigure(i, weight=1)

        # LISTAS DE LIQUIDACION
        self.lista_liquidacion_euros = []
        self.lista_numero_series_liquidacion = []
        self.lista_cartones_liquidacion = []

        # LISTAS DE VENTA
        self.lista_series_venta = []
        self.lista_Entry_carton_salida = []
        self.lista_carton_salida_2_al_cierre = []
        self.lista_carton_salida_siguiente_2_al_cierre = []

        # LISTAS ZONA DE BOTONES DE SUBIR Y BAJAR SERIES
        self.lista_etiquetas_series_preparadas = []


        #----FRAME ENCABEZAMIENTO CON ETIQUETA LIQUIDACIÓN---
        self.frame_columna1 = tk.Frame(self.ventana, bg="blue", bd=2, relief="groove")
        self.frame_columna1.grid(row=0, column=0, columnspan=11, sticky="nsew")
        self.etiqueta_zona_venta = tk.Label(self.frame_columna1, text="LIQUIDACIÓN", font=("Times New Roman",18,"bold"), bg="blue", fg="white" ) # Etiqueta numero de rango en liquidacion
        self.etiqueta_zona_venta.pack(fill="both", expand=True, pady=5)

        #----FRAME LIQUIACIÓN POR RANGOS---
        colores = ["gray59", "#C0C0C0"]
        for i in range(11):
            color = colores[i % 2]  # Alternar entre los dos colores

            self.frame_columna2 = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            self.frame_columna2.grid(row=1, column=i, sticky="nsew")  # sticky para expandir la columna

            if i == 0:
                # COLUMNA RANGO 1
                self.frame_columna2.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_rango1 = tk.Label(self.frame_columna2, text=f"RANGO 1", font=("Times New Roman",18,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rango1.pack(fill="both", expand=True, pady=10)#padx=10, pady=10,

                self.euros_liquidacion_rango1 = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_rango1.pack(fill="both", expand=True, pady=10)
                self.lista_liquidacion_euros.append(self.euros_liquidacion_rango1)

                self.etiqueta_series_liquidacion_rango1=tk.Label(self.frame_columna2, text = "SERIES + Pico", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_series_liquidacion_rango1.pack(fill="both", expand=True, pady=10)

                self.numero_series_liquidacion_rango1 = tk.Label(self.frame_columna2, text="0", fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
                self.numero_series_liquidacion_rango1.pack(fill="both", expand=True, pady=10)
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_rango1)

                self.etiqueta_del_al_liquidacion_rango1=tk.Label(self.frame_columna2, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_del_al_liquidacion_rango1.pack(fill="both", expand=True, pady=10)

                self.cartones_liquidacion_rango1 = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_rango1.pack(fill="both", expand=True, pady=10)
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_rango1)

                #linea_divisoria(self.frame_columna2) 

            if i > 0 and i < 9:
                # COLUMNA RANGOS DEL 2 AL 9
                self.etiqueta_rotulo_titulo_rangos = tk.Label(self.frame_columna2, text=f"RANGO {i}", bg=color, font=("Times New Roman",18,"bold")) # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rangos.pack(fill="both", expand=True, pady=10)

                self.euros_liquidacion_rangos = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_rangos.pack(fill="both", expand=True, pady=10)
                self.lista_liquidacion_euros.append(self.euros_liquidacion_rangos)

                self.etiqueta_series_liquidacion_rangos=tk.Label(self.frame_columna2, text = "SERIES", font=("Times New Roman", 13,"bold"), bg=color)
                self.etiqueta_series_liquidacion_rangos.pack(fill="both", expand=True, pady=10)

                self.numero_series_liquidacion_rangos = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.numero_series_liquidacion_rangos.pack(fill="both", expand=True, pady=10)
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_rangos)

                self.etiqueta_del_al_liquidacion_rangos=tk.Label(self.frame_columna2, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg=color)
                self.etiqueta_del_al_liquidacion_rangos.pack(fill="both", expand=True, pady=10)

                self.cartones_liquidacion_rangos = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_rangos.pack(fill="both", expand=True, pady=10)
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_rangos)

            if i == 9:
                #COLUMNA RANGO CIERRE
                self.frame_columna2.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_cierre = tk.Label(self.frame_columna2, text=f"CIERRE", font=("Times New Roman",18,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_cierre.pack(fill="both", expand=True, pady=10)

                self.euros_liquidacion_cierre = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_cierre.pack(fill="both", expand=True, pady=10)
                self.lista_liquidacion_euros.append(self.euros_liquidacion_cierre)

                self.etiqueta_series_liquidacion_rangos=tk.Label(self.frame_columna2, text = "SERIES + Pico", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_series_liquidacion_rangos.pack(fill="both", expand=True, pady=10)

                self.numero_series_liquidacion_cierre = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
                self.numero_series_liquidacion_cierre.pack(fill="both", expand=True, pady=10)
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_cierre)

                self.etiqueta_del_al_liquidacion_cierre=tk.Label(self.frame_columna2, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_del_al_liquidacion_cierre.pack(fill="both", expand=True, pady=10)

                self.cartones_liquidacion_cierre = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_cierre.pack(fill="both", expand=True, pady=10)
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_cierre)

            if i == 10:
                # COLUMNA TOTAL
                self.frame_columna2.config(bg="#0099ff")
                etiqueta_rotulo_titulo_total = tk.Label(self.frame_columna2, text=f"TOTAL", bg="#0099ff", font=("Times New Roman",18,"bold")) # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo_total.pack(fill="both", expand=True, pady=10)

                self.euros_liquidacion_total = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_total.pack(fill="both", expand=True, pady=10)
                self.lista_liquidacion_euros.append(self.euros_liquidacion_total)

                etiqueta_liquidacion_total=tk.Label(self.frame_columna2, text = "SERIES", font=("Times New Roman", 13,"bold"), bg="#0099ff")
                etiqueta_liquidacion_total.pack(fill="both", expand=True, pady=10)

                self.numero_series_liquidacion_total = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.numero_series_liquidacion_total.pack(fill="both", expand=True, pady=10)
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_total)

                self.etiqueta_del_al_liquidacion_total=tk.Label(self.frame_columna2, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg="#0099ff")
                self.etiqueta_del_al_liquidacion_total.pack(fill="both", expand=True, pady=10)

                self.cartones_liquidacion_total = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_total.pack(fill="both", expand=True, pady=10)
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_total)

        #---FRAME ENCABEZAMIENTO CON ETIQUETA VENTA---
        self.frame_columna3 = tk.Frame(self.ventana, bg="blue", bd=2, relief="groove")
        self.frame_columna3.grid(row=2, column=0, columnspan=11, sticky="nsew")
        self.etiqueta_zona_venta = tk.Label(self.frame_columna3, text=f"VENTA", font=("Times New Roman",18,"bold"), bg="blue", fg="white" ) # Etiqueta numero de rango en liquidacion
        self.etiqueta_zona_venta.pack(fill="both", expand=True, pady=5)


        #---FRAME VENTA POR RANGOS---
        for i in range(11):
            color = colores[i % 2]  # Alternar entre los dos colores

            self.frame_columna4 = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            self.frame_columna4.grid(row=3, column=i, sticky="nsew")

            if i == 0:
                # COLUMNA RANGO 1
                self.frame_columna4.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_rango1 = tk.Label(self.frame_columna4, text=f"SERIES", font=("Times New Roman",13,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rango1.pack(fill="both", expand=True, pady=10)

                self.etiqueta_numero_series_por_rango1_venta = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.etiqueta_numero_series_por_rango1_venta.pack(fill="both", expand=True, pady=10)
                self.lista_series_venta.append(self.etiqueta_numero_series_por_rango1_venta)

                self.etiquetas_salidas_venta1=tk.Label(self.frame_columna4, text = "SALIDAS", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
                self.etiquetas_salidas_venta1.pack(fill="both", expand=True, pady=10)

                for h in range(4):
                    self.Entry_carton_salida = tk.Entry(self.frame_columna4, text="", fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6, justify="right")
                    self.Entry_carton_salida.pack(fill="both", expand=True, pady=10)
                    self.lista_Entry_carton_salida.append(self.Entry_carton_salida)

            if i > 0 and i < 9:
                # COLUMNA RANGOS DEL 2 AL 9
                self.etiqueta_rotulo_titulo_rangos = tk.Label(self.frame_columna4, text=f"SERIES", bg=color, font=("Times New Roman",13,"bold")) # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rangos.pack(fill="both", expand=True, pady=10)

                self.etiqueta_numero_series_por_rangos_venta = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.etiqueta_numero_series_por_rangos_venta.pack(fill="both", expand=True, pady=10)
                self.lista_series_venta.append(self.etiqueta_numero_series_por_rangos_venta)

                self.etiquetas_salidas_ventas=tk.Label(self.frame_columna4, text = "SALIDAS", font=("Times New Roman", 15,"bold"), bg=color)
                self.etiquetas_salidas_ventas.pack(fill="both", expand=True, pady=10)

                for h in range(4):
                    #carton_salida = self.numero_carton_salida_2_9[indice_carton_salida]
                    self.etiqueta_carton_salida_2_9 = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                    self.etiqueta_carton_salida_2_9.pack(fill="both", expand=True, pady=10)
                    self.lista_carton_salida_2_al_cierre.append(self.etiqueta_carton_salida_2_9)


                    #carton_salida_siguiente_2_9 = self.numero_carton_salida_siguiente_2_9[indice_carton_salida]
                    self.etiqueta_carton_salida_siguiente_2_9 = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
                    self.etiqueta_carton_salida_siguiente_2_9.pack(fill="both", expand=True, pady=10)
                    self.lista_carton_salida_siguiente_2_al_cierre.append(self.etiqueta_carton_salida_siguiente_2_9)

                    self.etiqueta_vacia_2_9 = tk.Label(self.frame_columna4, text="", font=("Times New Roman",4,"bold"), bg=color)
                    self.etiqueta_vacia_2_9.pack()

                    # if self.bandera:
                    #     etiqueta_vacia.config(bg="#C0C0C0")
                    #     self.bandera = True
                    # else:
                    #     etiqueta_vacia.config(bg="gray59")
                    #     self.bandera = False

            if i == 9:
                #COLUMNA RANGO CIERRE
                self.frame_columna4.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_cierre = tk.Label(self.frame_columna4, text=f"SERIES", font=("Times New Roman",13,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_cierre.pack(fill="both", expand=True, pady=10)

                self.etiqueta_numero_series_por_rangos_cierre_venta = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.etiqueta_numero_series_por_rangos_cierre_venta.pack(fill="both", expand=True, pady=10)
                self.lista_series_venta.append(self.etiqueta_numero_series_por_rangos_cierre_venta)

                self.etiquetas_salidas_cierre=tk.Label(self.frame_columna4, text = "SALIDAS", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
                self.etiquetas_salidas_cierre.pack(fill="both", expand=True, pady=10)

                for r in range(4):
                    #carton_salida_cierre = self.etiqueta_numero_carton_salida_cierre[indice_carton_salida_cierre]
                    self.etiqueta_carton_salida_cierre = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                    self.etiqueta_carton_salida_cierre.pack(fill="both", expand=True, pady=10)
                    self.lista_carton_salida_2_al_cierre.append(self.etiqueta_carton_salida_cierre)


                    #carton_salida_siguiente_cierre = self.numero_carton_salida_siguiente_cierre[indice_carton_salida_cierre]
                    self.etiqueta_carton_salida_siguiente_cierre = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
                    self.etiqueta_carton_salida_siguiente_cierre.pack(fill="both", expand=True, pady=10)
                    self.lista_carton_salida_siguiente_2_al_cierre.append(self.etiqueta_carton_salida_siguiente_cierre)

                    self.etiqueta_vacia_cierre = tk.Label(self.frame_columna4, text="", font=("Times New Roman",4,"bold"), bg="#00FFFF")
                    self.etiqueta_vacia_cierre.pack(fill="both", expand=True, pady=10)
                    #indice_carton_salida_cierre += 1

            if i == 10:
                # COLUMNA PRECIOS
                self.frame_columna4.config(bg="#0099ff")
                etiqueta_rotulo_titulo_total = tk.Label(self.frame_columna4, text=f"PRECIOS", bg="#0099ff", font=("Times New Roman",13,"bold")) # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo_total.pack(fill="both", expand=True, pady=10)

                lista_precios = ["1,5€", "2€", "3€", "6€"]
                for i in lista_precios:
                    tk.Label(self.frame_columna4, text= i, font=("Times New Roman",20,"bold"), bg="#0099ff").pack(pady=15)

        #---FRAME ENCABEZAMIENTO CON ETIQUETA VENTA---
        self.frame_columna5 = tk.Frame(self.ventana, bg="blue", bd=2, relief="groove")
        self.frame_columna5.grid(row=4, column=0, columnspan=11, sticky="nsew")
        self.boton_cierre = tk.Button(self.frame_columna5, text=f"CERRAR", font=("Times New Roman",18,"bold"), bg="green", fg="white" )
        self.boton_cierre.pack(fill="both", expand=True, pady=10)


        self.lista_etiquetas_series_preparadas = []
        for i in range(11):
            color = colores[i % 2]  # Alternar entre los dos colores
            self.frame_botones = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            self.frame_botones.grid(row=5, column=i, sticky="nsew")
            if i == 0:
                etiqueta_rotulo_titulo = tk.Label(self.frame_botones, text=f"RANGO {i+1}", bg=color, font=("Times New Roman",15,"bold"))
                etiqueta_rotulo_titulo.pack(fill="both", expand=True, pady=10)
                
            
            elif i > 0 and i < 10:
                etiqueta_rotulo_titulo = tk.Label(self.frame_botones, text=f"RANGO {i}", bg=color, font=("Times New Roman",15,"bold"))
                etiqueta_rotulo_titulo.pack(fill="both", expand=True, pady=10)
                etiqueta_rotulo_series = tk.Label(self.frame_botones, text="SERIES", bg=color, font=("Arial",10,"bold"))
                etiqueta_rotulo_series.pack(fill="both", expand=True, pady=10)
                etiqueta_series = tk.Label(self.frame_botones, text="0", fg="blue", bg = "white", font=("Times New Roman",17,"bold"))
                etiqueta_series.pack(fill="both", expand=True, pady=10)
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

            # rotulos = ["HISTÓRICO", "RESET", "SALIR"]
            # colores_botones = ["Green", "#8B0000", "red"]
            # indice = 0
            # for j in range(3):
            #     boton = tk.Button(frame_botones, text=rotulos[indice], fg = "white", bg = colores_botones[indice], width=10, height=2,font=("Times New Roman",15,"bold"),cursor="hand2")
            #     boton.pack(pady = 10)
            #     indice += 1
            #     if j == 2:
            #         boton.config(command=lambda: cerrar_programa(self.ventana))

        self.frame_columna6 = tk.Frame(self.ventana, bg="blue", bd=2, relief="groove")
        self.frame_columna6.grid(row=6, column=0, columnspan=11, sticky="nsew")
        self.boton_cierre = tk.Button(self.frame_columna6, text=f"CERRAR", font=("Times New Roman",18,"bold"), bg="green", fg="white" )
        self.boton_cierre.pack(fill="both", expand=True, pady=10)
        self.boton_cierre = tk.Button(self.frame_columna6, text=f"CERRAR", font=("Times New Roman",18,"bold"), bg="green", fg="white" )
        self.boton_cierre.pack(fill="both", expand=True, pady=10)

    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    mi_ventana = Ventana()
    mi_ventana.ejecutar()

# En el frame_columna1 solo esta la etiqueta "LIQUIDACIÓN"
# En el frame_columna2 esta toda la informacion de liquidación
# En el fram_columna3 solo esta la etiqueta "VENTA"
# En el frame_columna4 esta toda la información de la proxima partida que se va a liquidar
# En el frame_columna5 solo esta el boton CERRAR
# En el frame_botones estan todos los botones de subir y bajas series
