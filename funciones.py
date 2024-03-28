import tkinter as tk

class MisFunciones:
    def __init__(self, ventana):
        self.ventana = ventana

    def incrementar_etiqueta(self, ident, etiqueta):
        """
        Incrementa el valor de la etiqueta en 1.
        """
        valor_actual = int(etiqueta["text"])
        nuevo_valor = valor_actual + 1
        etiqueta["text"] = str(nuevo_valor)

    def restar_etiqueta(self, ident, etiqueta):
        """
        restar el valor de la etiqueta en 1.
        """
        valor_actual = int(etiqueta["text"])
        if valor_actual == 0:
            pass
        else:
            nuevo_valor = valor_actual - 1
            etiqueta["text"] = str(nuevo_valor)

    def subir_a_venta(self, etiqueta1, etiqueta2):
        valor_actual = etiqueta1["text"]
        etiqueta2["text"] = valor_actual

    def suber_todo_a_venta(self, lista_series_botones, lista_series_venta, salida, lista_carton_salidas):

        #copia todas las series preparadas en el frame de los botones y las sube a venta
        for label_origen, label_destino in zip(lista_series_botones, lista_series_venta):
            texto_origen = label_origen.cget("text")
            label_destino.config(text=texto_origen)

        #--SALIDAS DE 1,5€
        #Calcula e imprime el carton de salida del rango 2, precio a 1,5€
        #Hay que calcular por separado el carton de salida del rango 2 por el pico de salida 
        salida_rango2 = (int(lista_series_venta[0].cget("text")) * 6) + self.pico_salida(salida[1].get())
        if lista_series_venta[1].cget("text") == "0":
            lista_carton_salidas[0].config(text = "0")
        else:
            lista_carton_salidas[0].config(text = salida_rango2)

        #Calcula e imprime el carton de salida del rango 3 al 9
        indice_carton_salida = 4
        for i in range(7):
            print(i)
            
            if lista_series_venta[i+2].cget("text") == "0":
                lista_carton_salidas[indice_carton_salida].config(text="0")
                indice_carton_salida += 4
            else:
                carton_salida = int(lista_carton_salidas[indice_carton_salida - 4].cget("text")) + int(lista_series_venta[i+1].cget("text")) * 6
                lista_carton_salidas[indice_carton_salida].config(text=carton_salida)
                indice_carton_salida += 4

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
        except:
            pass



    def cerrar_programa(self):
        self.ventana.destroy()
        exit()

    def on_click(self, identificador):
        i, j = map(int, identificador.split('_'))  # Descomponer el identificador único en i y j
        
        if identificador == 1_0:
            print(f"Botón Sube en el rango {i+1} ha sido presionado.")
        elif j == 1:
            print(f"Botón Venta en el rango {i+1} ha sido presionado.")
        else:
            print(f"Botón Baja en el rango {i+1} ha sido presionado.")