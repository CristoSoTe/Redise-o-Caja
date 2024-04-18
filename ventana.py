import tkinter as tk
from funciones import MisFunciones
import os

class Ventana():
    def __init__(self):
        #super().__init__()

        self.ventana = tk.Tk()
        self.ventana.attributes('-fullscreen', True)
        #self.ventana.geometry("1600x900")

        self.photoSube=tk.PhotoImage(file=r"/home/cristo/Descargas/Redise-o-Caja/flechaSube.png")#/home/redinf/Copilot/Redise-o-Caja/flechaSube.png
        self.photoBaja=tk.PhotoImage(file=r"/home/cristo/Descargas/Redise-o-Caja/flechaBaja.png")#/home/redinf/Copilot/Redise-o-Caja/flechaBaja.png

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
        self.lista_series_preparadas = []

        # LISTAS ZONA CM70
        self.lista_cm70 = []


        #----FRAME ENCABEZAMIENTO CON ETIQUETA LIQUIDACIÓN---
        self.frame_columna1 = tk.Frame(self.ventana, bg="blue")
        self.frame_columna1.grid(row=0, column=0, columnspan=11, sticky="nsew")
        self.etiqueta_zona_venta = tk.Label(self.frame_columna1, text="LIQUIDACIÓN", font=("Times New Roman",18,"bold"), bg="blue", fg="white" ) # Etiqueta numero de rango en liquidacion
        self.etiqueta_zona_venta.pack(fill="both", expand=True, pady=5)

        objeto_funciones = MisFunciones(self.ventana, self.lista_series_preparadas,self.lista_series_venta,self.lista_Entry_carton_salida,
            self.lista_carton_salida_2_al_cierre, self.lista_carton_salida_siguiente_2_al_cierre, self.lista_numero_series_liquidacion, self.lista_cm70, 
            self.lista_liquidacion_euros, self.lista_cartones_liquidacion)

        #----FRAME LIQUIACIÓN POR RANGOS---
        colores = ["gray59", "#C0C0C0"]
        for i in range(11):
            color = colores[i % 2]  # Alternar entre los dos colores

            self.frame_columna2 = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            self.frame_columna2.grid(row=1, column=i, sticky="nsew")  # 

            if i == 0:
                # COLUMNA RANGO 1
                self.frame_columna2.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_rango1 = tk.Label(self.frame_columna2, text=f"RANGO 1", font=("Times New Roman",18,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rango1.pack(expand=True)#, tk.BOTH

                self.euros_liquidacion_rango1 = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_rango1.pack(expand=True)
                self.lista_liquidacion_euros.append(self.euros_liquidacion_rango1)

                self.etiqueta_series_liquidacion_rango1=tk.Label(self.frame_columna2, text = "SERIES + Pico", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_series_liquidacion_rango1.pack(expand=True)

                self.numero_series_liquidacion_rango1 = tk.Label(self.frame_columna2, text="0", fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
                self.numero_series_liquidacion_rango1.pack(expand=True)
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_rango1)

                self.etiqueta_del_al_liquidacion_rango1=tk.Label(self.frame_columna2, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_del_al_liquidacion_rango1.pack(expand=True)

                self.cartones_liquidacion_rango1 = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_rango1.pack(expand=True)
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_rango1) 

            if i > 0 and i < 9:
                # COLUMNA RANGOS DEL 2 AL 9
                self.etiqueta_rotulo_titulo_rangos = tk.Label(self.frame_columna2, text=f"RANGO {i+1}", bg=color, font=("Times New Roman",18,"bold")) # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rangos.pack(expand=True)

                self.euros_liquidacion_rangos = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_rangos.pack(expand=True)
                self.lista_liquidacion_euros.append(self.euros_liquidacion_rangos)

                self.etiqueta_series_liquidacion_rangos=tk.Label(self.frame_columna2, text = "SERIES", font=("Times New Roman", 13,"bold"), bg=color)
                self.etiqueta_series_liquidacion_rangos.pack(expand=True)

                self.numero_series_liquidacion_rangos = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.numero_series_liquidacion_rangos.pack(expand=True)
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_rangos)

                self.etiqueta_del_al_liquidacion_rangos=tk.Label(self.frame_columna2, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg=color)
                self.etiqueta_del_al_liquidacion_rangos.pack(expand=True)

                self.cartones_liquidacion_rangos = tk.Label(self.frame_columna2, text="0", fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_rangos.pack(expand=True)
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_rangos)

            if i == 9:
                #COLUMNA RANGO CIERRE
                self.frame_columna2.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_cierre = tk.Label(self.frame_columna2, text=f"CIERRE", font=("Times New Roman",18,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_cierre.pack(expand=True)

                self.euros_liquidacion_cierre = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_cierre.pack(expand=True)
                self.lista_liquidacion_euros.append(self.euros_liquidacion_cierre)

                self.etiqueta_series_liquidacion_rangos=tk.Label(self.frame_columna2, text = "SERIES + Pico", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_series_liquidacion_rangos.pack(expand=True)

                self.numero_series_liquidacion_cierre = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
                self.numero_series_liquidacion_cierre.pack(expand=True)
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_cierre)

                self.etiqueta_del_al_liquidacion_cierre=tk.Label(self.frame_columna2, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg="#00FFFF")
                self.etiqueta_del_al_liquidacion_cierre.pack(expand=True)

                self.cartones_liquidacion_cierre = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_cierre.pack(expand=True)
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_cierre)

            if i == 10:
                # COLUMNA TOTAL
                self.frame_columna2.config(bg="#0099ff")
                etiqueta_rotulo_titulo_total = tk.Label(self.frame_columna2, text=f"TOTAL", bg="#0099ff", font=("Times New Roman",18,"bold")) # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo_total.pack(expand=True)

                self.euros_liquidacion_total = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                self.euros_liquidacion_total.pack(expand=True)
                self.lista_liquidacion_euros.append(self.euros_liquidacion_total)

                etiqueta_liquidacion_total=tk.Label(self.frame_columna2, text = "SERIES", font=("Times New Roman", 13,"bold"), bg="#0099ff")
                etiqueta_liquidacion_total.pack(expand=True)

                self.numero_series_liquidacion_total = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.numero_series_liquidacion_total.pack(expand=True)
                self.lista_numero_series_liquidacion.append(self.numero_series_liquidacion_total)

                self.etiqueta_del_al_liquidacion_total=tk.Label(self.frame_columna2, text = "DEL-AL", font=("Times New Roman", 13,"bold"), bg="#0099ff")
                self.etiqueta_del_al_liquidacion_total.pack(expand=True)

                self.cartones_liquidacion_total = tk.Label(self.frame_columna2, text=0, fg="blue", bg = "white", font=("Times New Roman",13,"bold"), width=8)
                self.cartones_liquidacion_total.pack(expand=True)
                self.lista_cartones_liquidacion.append(self.cartones_liquidacion_total)

        #---FRAME ENCABEZAMIENTO CON ETIQUETA VENTA---
        self.frame_columna3 = tk.Frame(self.ventana, bg="blue")
        self.frame_columna3.grid(row=2, column=0, columnspan=11, sticky="nsew")
        self.etiqueta_zona_venta = tk.Label(self.frame_columna3, text=f"VENTA", font=("Times New Roman",18,"bold"), bg="blue", fg="white" ) # Etiqueta numero de rango en liquidacion
        self.etiqueta_zona_venta.pack()


        #---FRAME VENTA POR RANGOS---
        for i in range(11):
            color = colores[i % 2]  # Alternar entre los dos colores

            self.frame_columna4 = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            self.frame_columna4.grid(row=3, column=i, sticky="nsew")

            if i == 0:
                # COLUMNA RANGO 1
                self.frame_columna4.config(bg="#00FFFF")
                self.etiqueta_rotulo_titulo_rango1 = tk.Label(self.frame_columna4, text=f"SERIES", font=("Times New Roman",13,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rango1.pack()

                self.etiqueta_numero_series_por_rango1_venta = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.etiqueta_numero_series_por_rango1_venta.pack()
                self.lista_series_venta.append(self.etiqueta_numero_series_por_rango1_venta)

                self.etiquetas_salidas_venta1=tk.Label(self.frame_columna4, text = "SALIDAS", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
                self.etiquetas_salidas_venta1.pack()

                for h in range(4):
                    self.Entry_carton_salida = tk.Entry(self.frame_columna4, text="", fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6, justify="right")
                    self.Entry_carton_salida.pack(pady=19)
                    self.lista_Entry_carton_salida.append(self.Entry_carton_salida)
                    self.lista_Entry_carton_salida[h].insert(0, 1)
                    #self.Entry_carton_salida.delete(0, tk.END)  # Borra el contenido actual del Entry
                    #self.Entry_carton_salida.insert(0, 4) 


            if i > 0 and i < 9:
                # COLUMNA RANGOS DEL 2 AL 9
                self.etiqueta_rotulo_titulo_rangos = tk.Label(self.frame_columna4, text=f"SERIES", bg=color, font=("Times New Roman",13,"bold")) # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_rangos.pack()

                self.etiqueta_numero_series_por_rangos_venta = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                self.etiqueta_numero_series_por_rangos_venta.pack()
                self.lista_series_venta.append(self.etiqueta_numero_series_por_rangos_venta)

                self.etiquetas_salidas_ventas=tk.Label(self.frame_columna4, text = "SALIDAS", font=("Times New Roman", 15,"bold"), bg=color)
                self.etiquetas_salidas_ventas.pack()

                for h in range(4):
                    #carton_salida = self.numero_carton_salida_2_9[indice_carton_salida]
                    self.etiqueta_carton_salida_2_9 = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                    self.etiqueta_carton_salida_2_9.pack()
                    self.lista_carton_salida_2_al_cierre.append(self.etiqueta_carton_salida_2_9)


                    #carton_salida_siguiente_2_9 = self.numero_carton_salida_siguiente_2_9[indice_carton_salida]
                    self.etiqueta_carton_salida_siguiente_2_9 = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
                    self.etiqueta_carton_salida_siguiente_2_9.pack()
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
                self.etiqueta_rotulo_titulo_cierre = tk.Label(self.frame_columna4, text="", font=("Times New Roman",13,"bold"), bg="#00FFFF") # Etiqueta numero de rango en liquidacion
                self.etiqueta_rotulo_titulo_cierre.pack(pady=15)

                self.etiqueta_numero_series_por_rangos_cierre_venta = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
                #self.etiqueta_numero_series_por_rangos_cierre_venta.pack()
                self.lista_series_venta.append(self.etiqueta_numero_series_por_rangos_cierre_venta)

                self.etiquetas_salidas_cierre=tk.Label(self.frame_columna4, text = "SALIDAS", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
                self.etiquetas_salidas_cierre.pack()

                for r in range(4):
                    #carton_salida_cierre = self.etiqueta_numero_carton_salida_cierre[indice_carton_salida_cierre]
                    self.etiqueta_carton_salida_cierre = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
                    self.etiqueta_carton_salida_cierre.pack()
                    self.lista_carton_salida_2_al_cierre.append(self.etiqueta_carton_salida_cierre)


                    #carton_salida_siguiente_cierre = self.numero_carton_salida_siguiente_cierre[indice_carton_salida_cierre]
                    self.etiqueta_carton_salida_siguiente_cierre = tk.Label(self.frame_columna4, text=0, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
                    self.etiqueta_carton_salida_siguiente_cierre.pack()
                    self.lista_carton_salida_siguiente_2_al_cierre.append(self.etiqueta_carton_salida_siguiente_cierre)

                    self.etiqueta_vacia_cierre = tk.Label(self.frame_columna4, text="", font=("Times New Roman",4,"bold"), bg="#00FFFF")
                    self.etiqueta_vacia_cierre.pack()
                    #indice_carton_salida_cierre += 1

            if i == 10:
                # COLUMNA PRECIOS
                self.frame_columna4.config(bg="#0099ff")
                etiqueta_rotulo_titulo_total = tk.Label(self.frame_columna4, text=f"PRECIOS", bg="#0099ff", font=("Times New Roman",13,"bold")) # Etiqueta numero de rango en liquidacion
                etiqueta_rotulo_titulo_total.pack(pady=20)

                lista_precios = ["1,5€", "2€", "3€", "6€"]
                for i in lista_precios:
                    tk.Label(self.frame_columna4, text= i, font=("Times New Roman",20,"bold"), bg="#0099ff").pack(pady=20)

        #---FRAME ENCABEZAMIENTO CON ETIQUETA VENTA---
        self.frame_columna5 = tk.Frame(self.ventana, bg="blue")
        self.frame_columna5.grid(row=4, column=0, columnspan=11, sticky="nsew")
        self.boton_cierre = tk.Button(self.frame_columna5, text=f"CERRAR", font=("Times New Roman",18,"bold"), bg="green", fg="white", command=objeto_funciones.cierre_partida)#lambda: self.lista_series_venta, self.lista_numero_series_liquidacion
        self.boton_cierre.pack(pady=2)

        #---FRAME BOTONES DE SUBIDA Y BAJADA DE SERIES
        for i in range(11):
            color = colores[i % 2]  # Alternar entre los dos colores
            self.frame_botones = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            self.frame_botones.grid(row=5, column=i, sticky="nsew")

            if i == 0:
                etiqueta_rotulo_titulo = tk.Label(self.frame_botones, text=f"RANGO {i+1}", bg=color, font=("Times New Roman",15,"bold"))
                etiqueta_rotulo_titulo.pack(expand=True)
                etiqueta_rotulo_series = tk.Label(self.frame_botones, text="SERIES", bg=color, font=("Arial",10,"bold"))
                etiqueta_rotulo_series.pack(expand=True)
                etiqueta_series = tk.Label(self.frame_botones, text="0", fg="blue", bg = "white", font=("Times New Roman",17,"bold"))
                etiqueta_series.pack(expand=True)
                self.lista_series_preparadas.append(etiqueta_series)

                boton_subir_rango1 = tk.Button(self.frame_botones, image=self.photoSube, command=lambda ident=0: objeto_funciones.incrementar_etiqueta(ident, self.lista_series_preparadas[0]))
                boton_subir_rango1.pack(pady=3, expand=True)
                boton_prepara_rango1 = tk.Button(self.frame_botones, text="VENTA", bg="Orange", command=lambda: objeto_funciones.subir_a_venta(self.lista_series_preparadas[0], self.lista_series_venta[0]))
                boton_prepara_rango1.pack(pady=3, expand=True)
                boton_bajar_rango1 = tk.Button(self.frame_botones, image=self.photoBaja, command=lambda ident =0: objeto_funciones.restar_etiqueta(ident, self.lista_series_preparadas[0]))
                boton_bajar_rango1.pack(pady=3, expand=True) 
            
            elif i > 0 and i < 9:
                etiqueta_rotulo_titulo = tk.Label(self.frame_botones, text=f"RANGO {i+1}", bg=color, font=("Times New Roman",15,"bold"))
                etiqueta_rotulo_titulo.pack(expand=True)
                etiqueta_rotulo_series = tk.Label(self.frame_botones, text="SERIES", bg=color, font=("Arial",10,"bold"))
                etiqueta_rotulo_series.pack(expand=True)
                etiqueta_series = tk.Label(self.frame_botones, text="0", fg="blue", bg = "white", font=("Times New Roman",17,"bold"))
                etiqueta_series.pack(expand=True)
                self.lista_series_preparadas.append(etiqueta_series)

                for j in range(3):
                    identificador = f"{i}_{j}"
                    if j == 0:
                        boton = tk.Button(self.frame_botones, image=self.photoSube, command=lambda ident=identificador, i=i: objeto_funciones.incrementar_etiqueta(ident, self.lista_series_preparadas[i]))
                    elif j == 1:
                        boton = tk.Button(self.frame_botones, text="VENTA", bg="Orange", command=lambda ident=identificador, i=i: objeto_funciones.subir_a_venta(self.lista_series_preparadas[i], self.lista_series_venta[i]))
                    else:
                        boton = tk.Button(self.frame_botones, image=self.photoBaja, command=lambda ident=identificador, i=i: objeto_funciones.restar_etiqueta(ident, self.lista_series_preparadas[i]))
                    
                    boton.pack(pady=3, expand=True)

            elif i == 9:
                #boton_comenzar = tk.Button(self.frame_botones, text="VENTA", bg="Orange", width=10, height=2, command=lambda: objeto_funciones.subir_todas_a_venta(self.lista_etiquetas_series_preparadas, self.lista_series_venta))
                boton_comenzar = tk.Button(self.frame_botones, text="VENTA", bg="Orange", width=10, height=2, command=objeto_funciones.subir_todo_a_venta)#=lambda: self.lista_series_preparadas,self.lista_series_venta, self.lista_Entry_carton_salida, self.lista_carton_salida_2_al_cierre
                boton_comenzar.pack(expand=True)

            elif i == 10:

                boton_atras = tk.Button(self.frame_botones, text="ATRÁS", bg="#e8e800", width=10, height=1)
                boton_atras.pack(expand=True)
                boton_historico = tk.Button(self.frame_botones, text="HISTÓRICO", bg="#00f078", width=10, height=1)
                boton_historico.pack(expand=True)
                boton_salir = tk.Button(self.frame_botones, text="SALIR", bg="red", width=10, height=1, command=objeto_funciones.cerrar_programa)
                boton_salir.pack(expand=True)

        #---FRAME DE RELLENO

        self.frame_columna6 = tk.Frame(self.ventana, bg="blue")
        self.frame_columna6.grid(row=6, column=0, columnspan=11, sticky="nsew")
        tk.Label(self.frame_columna6, text = "", bg="blue", fg= "white", font=("Times New Roman",1,"bold"), anchor="e", justify="right").pack(pady=1)

        #--- FRAME INFORMACION DEL cm70

        self.frame_columna7 = tk.Frame(self.ventana, bg="blue")#, bd=2, relief="groove"
        self.frame_columna7.grid(row=7, column=0, columnspan=11, sticky="nsew")
        self.etiquetas_premios = ["PRECIO", "DEL", "IMPRESOS", "RECAUDADO", "PREMIO LINEA", "PRIMA", "VENDIDOS", "AL", "INFORMATICOS","CAJA IMPRESOS", "PREMIO BINGO", "PRIMA EXTRA"]
        valor_fila = 0
        valor_columna = 0
        for etiqueta_premio in self.etiquetas_premios:
            tk.Label(self.frame_columna7, text = etiqueta_premio, bg="blue", fg= "white", font=("Times New Roman",13,"bold"), anchor="e", justify="right").grid(row = valor_fila, column = valor_columna, sticky = "ew", padx= 10)
            valor_columna += 1
            entrada = tk.Entry(self.frame_columna7, font=("Times New Roman",13,"bold"), justify="right", width=14)
            entrada.grid(row = valor_fila, column = valor_columna, sticky = "ew", pady=1)
            valor_columna += 1

            self.lista_cm70.append(entrada)
            

            if valor_columna > 11:
                valor_fila = 1
                valor_columna = 0
        self.lista_cm70[0].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[0].insert(0, 1.5)
        self.lista_cm70[1].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[1].insert(0, 3)
        self.lista_cm70[2].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[2].insert(0, 424)
        self.lista_cm70[3].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[3].insert(0, 636)
        self.lista_cm70[4].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[4].insert(0, 110)
        self.lista_cm70[5].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[5].insert(0, 100)
        self.lista_cm70[6].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[6].insert(0, 428)
        self.lista_cm70[7].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[7].insert(0, 426)
        self.lista_cm70[8].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[8].insert(0, 4)
        self.lista_cm70[9].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[9].insert(0, 630)
        self.lista_cm70[10].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[10].insert(0, 250)
        self.lista_cm70[11].delete(0, tk.END)  # Borra el contenido actual del Entry
        self.lista_cm70[11].insert(0, 100)
        #self.entradas[12].delete(0, tk.END)  # Borra el contenido actual del Entry
        #self.entradas[12].insert(0, 3)
        

        self.frame_columna8 = tk.Frame(self.ventana, bg="blue")
        self.frame_columna8.grid(row=8, column=0, columnspan=11, sticky="nsew")
        tk.Label(self.frame_columna8, text = "", bg="blue", fg= "white", font=("Times New Roman",1,"bold"), anchor="e", justify="right").pack(pady=1)


    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    mi_ventana = Ventana()
    mi_ventana.ejecutar()

# En el frame_columna1 solo esta la etiqueta "LIQUIDACIÓN"
# En el frame_columna2 esta toda la informacion de liquidación
# En el frame_columna3 solo esta la etiqueta "VENTA"
# En el frame_columna4 esta toda la información de la proxima partida que se va a liquidar
# En el frame_columna5 solo esta el boton CERRAR
# En el frame_botones estan todos los botones de subir y bajas series
# El frame_columna8 es de relleno
# En El frame_columna7 esta la informacion del CM70
# El frame_columna8 es de relleno
