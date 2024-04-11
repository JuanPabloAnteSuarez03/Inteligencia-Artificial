from nave import Nave

class NaveController:
    def __init__(self):
        self.nave = None

    def crear_nave(self, fila, columna):
        self.nave = Nave(fila, columna)

    def obtener_posicion_nave(self):
        return self.nave.get_posicion()
