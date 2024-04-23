import tkinter as tk

class MisFunciones:
    def __init__(self, ventana, lista_series_botones, lista_series_venta, lista_Entry_carton_salida, lista_carton_salidas, 
        lista_carton_salida_siguiente, lista_series_liquidacion, datos_cm70, euros, cartones_rangos, frame_1, etiqueta_liquidacion,
        columnas_venta, etiqueta_vacia_venta):
        self.ventana = ventana
        self.lista_series_botones = lista_series_botones
        self.lista_series_venta = lista_series_venta
        self.salida = lista_Entry_carton_salida
        self.lista_carton_salidas = lista_carton_salidas
        self.lista_carton_salida_siguiente = lista_carton_salida_siguiente
        self.lista_series_liquidacion = lista_series_liquidacion
        self.datos_cm70 = datos_cm70
        self.euros = euros
        self.cartones_rangos = cartones_rangos
        self.frame1 = frame_1
        self.etiqueta_liquidacion = etiqueta_liquidacion
        self.columnas_venta = columnas_venta
        self.etiqueta_vacia_venta = etiqueta_vacia_venta

    def incrementar_etiqueta(self, ident, etiqueta):
        #Incrementa el valor de la etiqueta en 1.
        valor_actual = int(etiqueta["text"])
        nuevo_valor = valor_actual + 1
        etiqueta["text"] = str(nuevo_valor)
        self.cartones_salidas_siguiete()

    def restar_etiqueta(self, ident, etiqueta):
        #restar el valor de la etiqueta en 1.
        valor_actual = int(etiqueta["text"])
        if valor_actual == 0:
            pass
        else:
            nuevo_valor = valor_actual - 1
            etiqueta["text"] = str(nuevo_valor)
        self.cartones_salidas_siguiete()

    def subir_a_venta(self, etiqueta1, etiqueta2):
        #---SUBE A VENTA POR RANGO
        valor_actual = etiqueta1["text"]
        etiqueta2["text"] = valor_actual
        self.cartones_salidas()
        self.cartones_salidas_siguiete()
        self.colores()
        
    def subir_todo_a_venta(self):
        #copia todas las series preparadas en el frame de los botones y las sube a venta
        for label_origen, label_destino in zip(self.lista_series_botones, self.lista_series_venta):
            texto_origen = label_origen.cget("text")
            label_destino.config(text=texto_origen)
        self.cartones_salidas()
        self.cartones_salidas_siguiete()
        self.colores()

    def cartones_salidas(self):
        indice_carton_salida = 4 #esta variable es para saltar a la casilla que le corresponde en el carton de salida
        valor = 1#Esta variable es para corregir cuando un rango no tiene series
        for i in range(4):
            #Calcula e imprime el carton de salida del rango 2 de todos los precios separado del resto de rangos por el pico de salida del rango 1
            salida_rango2 = (int(self.lista_series_venta[0].cget("text")) * 6) + self.pico_salida(self.salida[i].get()) + int(self.salida[i].get())
            if self.lista_series_venta[1].cget("text") == 0 or self.lista_series_venta[1].cget("text") == "0":
                self.lista_carton_salidas[i].config(text = "0")
                salida_rango_anterior = int(self.salida[i].get())
                valor -= 1
            else:
                self.lista_carton_salidas[i].config(text = salida_rango2)
                salida_rango_anterior = salida_rango2
                valor = 1
                
            #Calcula e imprime el carton de salida del rango 3 al 9 de todos los precios
            for h in range(7):
                if self.lista_series_venta[h+2].cget("text") == 0 or self.lista_series_venta[h+2].cget("text") == "0":
                    self.lista_carton_salidas[indice_carton_salida].config(text="0")
                    valor -= 1
                else:
                    carton_salida = int(salida_rango_anterior) + int(self.lista_series_venta[h+valor].cget("text")) * 6
                    self.lista_carton_salidas[indice_carton_salida].config(text=carton_salida)
                    valor = 1
                    salida_rango_anterior = carton_salida
                    
                # Calculamos e imprimimos el carton de salida del cierre de todos los precios
                if indice_carton_salida == 28:
                    salida_cierre = salida_rango_anterior + int(self.lista_series_venta[h+valor+1].cget("text")) * 6
                    self.lista_carton_salidas[32].config(text=salida_cierre)
                    valor = 1
                    indice_carton_salida = 1
                elif indice_carton_salida == 29:
                    salida_cierre = salida_rango_anterior + int(self.lista_series_venta[h+valor+1].cget("text")) * 6
                    self.lista_carton_salidas[33].config(text=salida_cierre)
                    valor = 1
                    indice_carton_salida = 2
                elif indice_carton_salida == 30:
                    salida_cierre = salida_rango_anterior + int(self.lista_series_venta[h+valor+1].cget("text")) * 6
                    self.lista_carton_salidas[34].config(text=salida_cierre)
                    valor = 1
                    indice_carton_salida = 3
                elif indice_carton_salida == 31:
                    salida_cierre = salida_rango_anterior + int(self.lista_series_venta[h+valor+1].cget("text")) * 6
                    self.lista_carton_salidas[35].config(text=salida_cierre)
                    valor = 1
                    break

                indice_carton_salida += 4

    def cartones_salidas_siguiete(self):
        indice_carton_salida = 4 #esta variable es para saltar a la casilla que le corresponde en el carton de salida
        valor = 1#Esta variable es para corregir cuando un rango no tiene series
        for i in range(4):
            #Calcula e imprime el carton de salida del rango 2 de todos los precios separado del resto de rangos por el pico de salida del rango 1
            salida_rango2 = (int(self.lista_series_botones[0].cget("text")) * 6) + self.pico_salida(self.salida[i].get()) + int(self.salida[i].get())
            if self.lista_series_botones[1].cget("text") == 0 or self.lista_series_botones[1].cget("text") == "0":
                self.lista_carton_salida_siguiente[i].config(text = "0")
                salida_rango_anterior = int(self.salida[i].get())
                valor -= 1
            else:
                self.lista_carton_salida_siguiente[i].config(text = salida_rango2)
                salida_rango_anterior = salida_rango2
                valor = 1
                
            #Calcula e imprime el carton de salida del rango 3 al 9 de todos los precios
            for h in range(7):
                if self.lista_series_botones[h+2].cget("text") == 0 or self.lista_series_botones[h+2].cget("text") == "0":
                    self.lista_carton_salida_siguiente[indice_carton_salida].config(text="0")
                    valor -= 1
                else:
                    carton_salida = int(salida_rango_anterior) + int(self.lista_series_botones[h+valor].cget("text")) * 6
                    self.lista_carton_salida_siguiente[indice_carton_salida].config(text=carton_salida)
                    valor = 1
                    salida_rango_anterior = carton_salida
                    
                # Calculamos e imprimimos el carton de salida del cierre de todos los precios
                if indice_carton_salida == 28:
                    salida_cierre = salida_rango_anterior + int(self.lista_series_botones[h+valor+1].cget("text")) * 6
                    self.lista_carton_salida_siguiente[32].config(text=salida_cierre)
                    valor = 1
                    indice_carton_salida = 1
                elif indice_carton_salida == 29:
                    salida_cierre = salida_rango_anterior + int(self.lista_series_botones[h+valor+1].cget("text")) * 6
                    self.lista_carton_salida_siguiente[33].config(text=salida_cierre)
                    valor = 1
                    indice_carton_salida = 2
                elif indice_carton_salida == 30:
                    salida_cierre = salida_rango_anterior + int(self.lista_series_botones[h+valor+1].cget("text")) * 6
                    self.lista_carton_salida_siguiente[34].config(text=salida_cierre)
                    valor = 1
                    indice_carton_salida = 3
                elif indice_carton_salida == 31:
                    salida_cierre = salida_rango_anterior + int(self.lista_series_botones[h+valor+1].cget("text")) * 6
                    self.lista_carton_salida_siguiente[35].config(text=salida_cierre)
                    valor = 1
                    break

                indice_carton_salida += 4

    def cierre_partida(self):#, lista_series_venta, lista_series_liquidacion
        pico_salida = self.pico_salida(self.datos_cm70[1].get())
        pico_cierre = self.pico_cierre(self.datos_cm70[7].get())

        #Aqui sube todas las series de la zona de venta a la zona de liquidacion del rango 1 al 9 
        for label_origen, label_destino in zip(self.lista_series_venta, self.lista_series_liquidacion):
            texto_origen = label_origen.cget("text")
            label_destino.config(text=texto_origen)
        
        #Calcula series del rango de cierre
        series_asignadas = 0
        #Primero sumamos las series que tiene asignado los rangos del 1 al 9
        for i in range(9):
            series_asignadas += int(self.lista_series_liquidacion[i].cget("text"))
        series_cierre = 0
        #Despues calculamos las series que le quedan al cierre
        for i in range(9):
            series_cierre = int(((float(self.datos_cm70[2].get())- pico_salida - pico_cierre)) / 6) - series_asignadas
        self.lista_series_liquidacion[9].config(text=f"{series_cierre}+{pico_cierre}")

        #Se corrige el numero de series en el rango 1 para poner el pico de salida en el texto
        self.lista_series_liquidacion[0].config(text=f"{self.lista_series_liquidacion[0].cget('text')}+{pico_salida}")

        #Calculamos el total de series y la imprimimos
        total_series = series_asignadas + series_cierre
        self.lista_series_liquidacion[10].config(text=total_series)

        self.cartones_por_rango()

    def cartones_por_rango(self):
        carton_inicial = int(self.datos_cm70[1].get())
        pico_inicial = self.pico_salida(carton_inicial)

        #La etiqueta numero de series del rango 1 contiene el numero de series, un guion y el pico de salida por lo que extraemos el numero de series
        self.series = self.lista_series_liquidacion[0].cget("text").split("+")[0]
        #Calculamos los cartones del rango 1 y los imprimimos
        carton_final_R1 = carton_inicial + pico_inicial - 1 + int(self.series) * 6
        self.cartones_rangos[0].config(text=str(carton_inicial) + "-" + str(carton_final_R1))

        #Calculamos los cartones del rango 2 al 9
        carton_final_rango_anterior = carton_final_R1
        for i in range(8):
            if self.lista_series_liquidacion[i+1].cget("text") == "0":
                self.cartones_rangos[i+1].config(text="0-0")
            else:
                carton_final_rango = int(self.lista_series_liquidacion[i+1].cget("text")) * 6 + carton_final_rango_anterior
                self.cartones_rangos[i+1].config(text=str(carton_final_rango_anterior + 1) + "-" + str(carton_final_rango))
                carton_final_rango_anterior = carton_final_rango

        #Imprimimos los cartones asignados al cierre
        self.cartones_rangos[9].config(text=str(carton_final_rango_anterior + 1) + "-" + self.datos_cm70[7].get())

        #Imprimimos los cartones totales
        self.cartones_rangos[10].config(text=self.datos_cm70[1].get() + "-" + self.datos_cm70[7].get())

        self.calcula_liquidacion(pico_inicial)

    def calcula_liquidacion(self, pico_inicial):
        pico_cierre = self.pico_cierre(self.datos_cm70[7].get())
        #Calcula la liquidacion del rango 1 por tener pico
        euros_R1 = str("{:.2f}".format((int(self.series) * 6 + int(pico_inicial)) * float(self.datos_cm70[0].get())))
        simbolo = "€"
        self.euros[0].config(text=euros_R1 + simbolo)

        #Calcula la liquidacion del rango 2 al 9
        for i in range(8):
            euros_R2_al_9 = str("{:.2f}".format(int(self.lista_series_liquidacion[i+1].cget("text")) * 6 * float(self.datos_cm70[0].get())))
            self.euros[i+1].config(text=euros_R2_al_9 + simbolo)

        #Calcula liquidacion del cierre por tener pico
        self.extrae_series_cierre = self.lista_series_liquidacion[9].cget("text").split("+")[0]
        euros_cierre = str("{:.2f}".format((int(self.extrae_series_cierre) * 6 + int(pico_cierre)) * float(self.datos_cm70[0].get())))
        simbolo = "€"
        self.euros[9].config(text=euros_cierre + simbolo)

        #Calcula el total liquidacion
        total_liquidacion =  str("{:.2f}".format(float(self.datos_cm70[0].get()) * int(self.datos_cm70[2].get())))
        self.euros[10].config(text=total_liquidacion + simbolo)

        self.colores()

    def colores(self):
        colores = ["#C0C0C0", "gray59"]

        if self.datos_cm70[0].get() == "1.5":
            self.frame1.config(bg="blue")
            self.etiqueta_liquidacion.config(bg="blue")
        elif self.datos_cm70[0].get() == "2":
            self.frame1.config(bg="#E7692C")
            self.etiqueta_liquidacion.config(bg="#E7692C")
        elif self.datos_cm70[0].get() == "3":
            self.frame1.config(bg="#AF45D2")
            self.etiqueta_liquidacion.config(bg="#AF45D2")
        elif self.datos_cm70[0].get() == "6":
            self.frame1.config(bg="#893E65")
            self.etiqueta_liquidacion.config(bg="#893E65")
        for i in range(8):
            color = colores[i % 2]
            if int(self.lista_series_venta[i+1].cget("text")) != 0:
                self.columnas_venta[i+1].config(bg="#00FFFF")
                color1 = self.columnas_venta[i+1].cget("bg")
                self.etiqueta_vacia_venta.config(text=color1)
            else:
                self.columnas_venta[i+1].config(bg=color)
                self.etiqueta_vacia_venta.config(bg=color)

    def pico_salida(self, salida):
        try:
            if salida == 0 or salida == "":
                pass
            else:
                self.pico_sal = 7 - (int(salida) % 6)
                if self.pico_sal == 7:
                    self.pico_sal = 1
                elif self.pico_sal == 6:
                    self.pico_sal = 0
                return self.pico_sal
        except:
            pass

    def pico_cierre(self, cierre):
        try:
            if cierre == "0" or cierre == "":
                pass
            else:
                self.pico_cie = (int(cierre) % 6)
                return self.pico_cie
        except:
            pass
            
    def cerrar_programa(self):
        self.ventana.destroy()
        exit()