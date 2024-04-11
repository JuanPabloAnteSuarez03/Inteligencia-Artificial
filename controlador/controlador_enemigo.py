from enemigo import Enemigo

class EnemigoController:
    def __init__(self):
        self.enemigo = None

    def crear_enemigo(self, fila, columna):
        self.enemigo = Enemigo(fila, columna)

    def obtener_posicion_enemigo(self):
        return self.enemigo.get_posicion()
