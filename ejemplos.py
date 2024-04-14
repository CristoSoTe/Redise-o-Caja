class Ventana():
    def __init__(self):
        #super().__init__()

        self.ventana = tk.Tk()
        self.ventana.attributes('-fullscreen', True)

        self.lista_series_venta = []
        self.lista_series_preparadas = []

        objeto_funciones = MisFunciones(self.ventana, self.lista_series_preparadas,self.lista_series_venta)

        boton_comenzar = tk.Button(self.frame_botones, text="VENTA", bg="Red", width=10, height=2, command=objeto_funciones.subir_todo_a_venta)

class MisFunciones:
    def __init__(self, ventana, lista_series_botones, lista_series_venta):
        self.ventana = ventana
        self.lista_series_botones = lista_series_botones
        self.lista_series_venta = lista_series_venta

    def subir_todo_a_venta(self):
        for label_origen, label_destino in zip(self.lista_series_botones, self.lista_series_venta):
            texto_origen = label_origen.cget("text")
            label_destino.config(text=texto_origen)