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

    def suber_todo_a_venta(self, lista_origen, lista_destino, salida):

        for label_origen, label_destino in zip(lista_origen, lista_destino):
            texto_origen = label_origen.cget("text")
            label_destino.config(text=texto_origen)
        salida_rango1=salida[1].get()
        self.pico_salida(salida_rango1)

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
        print(self.pico_sal)

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