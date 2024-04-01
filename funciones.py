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
        #---SUBE A VENTA POR RANGO
        valor_actual = etiqueta1["text"]
        etiqueta2["text"] = valor_actual

    def subir_todas_a_venta(self, lista_inferior, lista_venta):
        #---SUBE TODOS LOS RANGOS A VENTA
        for i in range(len(lista_inferior)):
            texto_origen = lista_inferior[i].cget("text")
            lista_venta[i].config(text=texto_origen)

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