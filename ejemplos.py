import tkinter as tk

class Ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana con Etiquetas y Botones")
        self.ventana.geometry("1600x900")

        self.ventana.grid_rowconfigure(0, weight=1)
        for i in range(10):
            self.ventana.grid_columnconfigure(i, weight=1)

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

if __name__ == "__main__":
    ventana = Ventana()
    ventana.ventana.mainloop()