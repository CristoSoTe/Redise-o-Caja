import ctypes
from ctypes import wintypes

# Definir la estructura de datos para obtener la información del esquema de colores
class CurrentConsoleFontEx(ctypes.Structure):
    _fields_ = [('nFont', ctypes.wintypes.DWORD),
                ('dwFontSize', wintypes._COORD)]

# Obtener el manejador de la consola
hOut = ctypes.windll.kernel32.GetStdHandle(-11)

# Obtener el esquema de colores actual
info = CurrentConsoleFontEx()
ctypes.windll.kernel32.GetCurrentConsoleFontEx(hOut, False, ctypes.byref(info))

# Imprimir el tamaño de la fuente y los colores actuales
print("Tamaño de la fuente:", info.dwFontSize.X, "x", info.dwFontSize.Y)
print("Esquema de colores actual:", ctypes.windll.kernel32.GetConsoleScreenBufferInfoEx(hOut).wAttributes)