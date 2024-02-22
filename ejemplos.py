import tkinter as tk

class AplicacionTkinter:
    def __init__(self, master):
        self.master = master
        self.ventana = tk.Frame(master)
        self.ventana.pack()

        # Definir una lista de funciones
        funciones = [self.funcion1, self.funcion2, self.funcion3, self.funcion4, self.funcion5, self.funcion6, self.funcion7, self.funcion8, self.funcion9, self.funcion10]

        colores = ["red", "blue"]  # Colores para los frames

        for i in range(10):
            color = colores[i % 2]  # Alternar entre los dos colores
            frame_botones = tk.Frame(self.ventana, bg=color, bd=2, relief="groove")
            frame_botones.grid(row=2, column=i, sticky="nsew")  # sticky para expandir la columna
            for j in range(3):
                num_funcion = i * 3 + j
                boton = tk.Button(frame_botones, text=f"Botón {num_funcion + 1}", command=funciones[num_funcion])
                boton.pack()

    def funcion1(self):
        print("Función 1")

    def funcion2(self):
        print("Función 2")

    def funcion3(self):
        print("Función 3")

    def funcion4(self):
        print("Función 4")

    def funcion5(self):
        print("Función 5")

    def funcion6(self):
        print("Función 6")

    def funcion7(self):
        print("Función 7")

    def funcion8(self):
        print("Función 8")

    def funcion9(self):
        print("Función 9")

    def funcion10(self):
        print("Función 10")

def main():
    root = tk.Tk()
    app = AplicacionTkinter(root)
    root.mainloop()

if __name__ == "__main__":
    main()