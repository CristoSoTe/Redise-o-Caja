def incrementar_etiqueta(etiqueta):
    """
    Incrementa el valor de la etiqueta en 1.
    """
    valor_actual = int(etiqueta["text"])
    nuevo_valor = valor_actual + 1
    etiqueta["text"] = str(nuevo_valor)

def restar_etiqueta(etiqueta):
    """
    restar el valor de la etiqueta en 1.
    """
    valor_actual = int(etiqueta["text"])
    if valor_actual == 0:
        pass
    else:
        nuevo_valor = valor_actual - 1
        etiqueta["text"] = str(nuevo_valor)

def subir_a_venta(etiqueta1, etiqueta2):
    valor_actual = etiqueta1["text"]
    etiqueta2["text"] = valor_actual

def cerrar_programa(ventana):
    ventana.destroy()
    exit()