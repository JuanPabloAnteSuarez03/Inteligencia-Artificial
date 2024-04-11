from grogu import Grogu

class GroguController:
    def __init__(self):
        self.grogu = None

    def crear_grogu(self, fila, columna):
        self.grogu = Grogu(fila, columna)

    def obtener_posicion_grogu(self):
        return self.grogu.get_posicion()