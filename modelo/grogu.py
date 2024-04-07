class Grogu:
    def __init__(self, fila_inicial, columna_inicial):
        self.fila = fila_inicial
        self.columna = columna_inicial
    
    def get_posicion(self):
        return self.fila, self.columna
    
    def set_posicion(self, fila, columna):
        self.fila = fila
        self.columna = columna


# # Ejemplo de uso
# grogu = Grogu(0, 9)  # Supongamos que Grogu está en la fila 0, columna 9
# print("Posición inicial de Grogu:", grogu.get_posicion())

# # Moviendo a Grogu a una nueva posición
# grogu.set_posicion(5, 5)
# print("Nueva posición de Grogu:", grogu.get_posicion())
