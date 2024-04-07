class Enemigo:
    def __init__(self, fila_inicial, columna_inicial):
        self.fila = fila_inicial
        self.columna = columna_inicial
    
    def get_posicion(self):
        return self.fila, self.columna
    
    def set_posicion(self, fila, columna):
        self.fila = fila
        self.columna = columna


# # Ejemplo de uso
# enemigo = Enemigo(2, 4)  # Supongamos que hay un enemigo en la fila 2, columna 4
# print("Posición inicial del enemigo:", enemigo.get_posicion())

# # Moviendo al enemigo a una nueva posición
# enemigo.set_posicion(5, 7)
# print("Nueva posición del enemigo:", enemigo.get_posicion())
