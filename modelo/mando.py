class Mando:
    def __init__(self, fila_inicial, columna_inicial):
        self.fila = fila_inicial
        self.columna = columna_inicial
    
    def get_posicion(self):
        return self.fila, self.columna
    
    def set_posicion(self, fila, columna):
        self.fila_inicial = fila
        self.columna_inicial = columna

    def mover_arriba(self):
        self.fila -= 1
    
    def mover_abajo(self):
        self.fila += 1
    
    def mover_izquierda(self):
        self.columna -= 1
    
    def mover_derecha(self):
        self.columna += 1


# Ejemplo de uso
mando = Mando(3, 0)  # Supongamos que Mando comienza en la fila 3, columna 0
print("Posición inicial de Mando:", mando.get_posicion())

mando.mover_abajo()
print("Mando se mueve hacia abajo. Nueva posición:", mando.get_posicion())

mando.mover_derecha()
print("Mando se mueve hacia la derecha. Nueva posición:", mando.get_posicion())
