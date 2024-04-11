from mando import Mando

class MandoController:
    def __init__(self):
        self.mando = None

    def crear_mando(self, fila, columna):
        self.mando = Mando(fila, columna)

    def obtener_posicion_mando(self):
        return self.mando.get_posicion()