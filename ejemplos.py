import tkinter as tk

class Ventana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.attributes('-fullscreen', True)
        self.screen_height = self.ventana.winfo_screenheight()

        # Lista de frames
        self.frames = []

        # Crear siete frames y widgets
        self.crear_frames_y_widgets()

    def crear_frames_y_widgets(self):
        num_frames = 7  # Número total de frames
        frame_height = self.screen_height // num_frames  # Altura de cada frame

        for i in range(num_frames):
            frame = tk.Frame(self.ventana, bg="blue", bd=2, relief="groove")
            frame.grid(row=i, column=0, sticky="nsew")

            # Configurar altura de cada frame
            frame.config(height=frame_height)

            # Agregar widgets a cada frame
            self.agregar_widgets(frame)

            self.frames.append(frame)

        # Configurar el peso de la fila para que los frames se expandan verticalmente
        self.ventana.grid_rowconfigure((i for i in range(num_frames)), weight=1)

    def agregar_widgets(self, frame):
        # Agregar widgets a cada frame
        etiqueta = tk.Label(frame, text="Etiqueta", font=("Arial", 16), bg="blue", fg="white")
        etiqueta.pack(fill="both", expand=True, pady=10)

        boton = tk.Button(frame, text="Botón", font=("Arial", 14))
        boton.pack(fill="both", expand=True, pady=5)

        # Agregar más widgets según sea necesario

    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    mi_ventana = Ventana()
    mi_ventana.ejecutar()