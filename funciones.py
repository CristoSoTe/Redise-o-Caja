import tkinter as tk

class MisFunciones:
    def __init__(self, ventana, lista_series_botones, lista_series_venta, lista_Entry_carton_salida, lista_carton_salidas, 
        lista_carton_salida_siguiente, lista_series_liquidacion, datos_cm70, euros, cartones_rangos):
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
        
    def subir_todo_a_venta(self):
        #copia todas las series preparadas en el frame de los botones y las sube a venta
        for label_origen, label_destino in zip(self.lista_series_botones, self.lista_series_venta):
            texto_origen = label_origen.cget("text")
            label_destino.config(text=texto_origen)
        self.cartones_salidas()
        self.cartones_salidas_siguiete()

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
    def calcula_liquidacion(self, pico_inicial):
        #Calcula la liquidacion del rango 1 por tener pico
        euros_R1 = str("{:.2f}".format((int(self.lista_series_liquidacion[0].cget("text")) * 6 + int(pico_inicial)) * float(self.datos_cm70[0].get())))
        simbolo = "€"
        self.euros[0].config(text=euros_R1 + simbolo)

        #Calcula la liquidacion del rango 2 al 9
        for i in range(8):
            euros_R2_al_9 = str("{:.2f}".format(int(self.lista_series_liquidacion[i+1].cget("text")) * 6 * float(self.datos_cm70[0].get())))
            self.euros[i+1].config(text=euros_R2_al_9 + simbolo)

    def cartones_por_rango(self):
        carton_inicial = int(self.salida[0].get())
        pico_inicial = self.pico_salida(carton_inicial)
        carton_final_R1 = carton_inicial + pico_inicial - 1 + int(self.lista_series_liquidacion[0].cget("text")) * 6
        self.cartones_rangos[0].config(text=str(carton_inicial) + " - " + str(carton_final_R1))
        self.calcula_liquidacion(pico_inicial)


    def cierre_partida(self):#, lista_series_venta, lista_series_liquidacion
        for label_origen, label_destino in zip(self.lista_series_venta, self.lista_series_liquidacion):
            texto_origen = label_origen.cget("text")
            label_destino.config(text=texto_origen)

        #Calcula series del rango de cierre
        #Estasintentyando calcular las series de cierre, no has probado el codigo de la linea 174 a 177
        series_cierre = 0
        for i in range(9):
            series_cierre += (float(self.datos_cm70[0].get()) - int(self.lista_series_liquidacion[i].cget("text")) - self.pico_salida(self.datos_cm70[1].get()) - self.pico_cierre(self.datos_cm70[7].get())) / 6
            print(series_cierre)
            self.lista_series_liquidacion[9].config(text=series_cierre)
        self.cartones_por_rango()

        # Calculamos e imprimimos el total de series al cierre
        #total_series = 0
        #for i in range(9):
            #total_series += int(lista_series_venta[i].cget("text"))
            #lista_series_venta[9].config(text=total_series)

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
                print(self.pico_cie)
                return self.pico_cie
        except:
            pass
            
    def cerrar_programa(self):
        self.ventana.destroy()
        exit()