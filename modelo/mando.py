from arbol import Nodo  # Importamos la clase Nodo

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
 
    def get_movimientos_posibles(self, matriz):
        movimientos = []

        if self.columna > 0 and matriz[self.fila][self.columna - 1] != 1:  # Mover Izquierda
            movimientos.append((self.fila, self.columna - 1))
        if self.fila > 0 and matriz[self.fila - 1][self.columna] != 1:  # Mover Arriba
            movimientos.append((self.fila - 1, self.columna))
        if self.fila < len(matriz) - 1 and matriz[self.fila + 1][self.columna] != 1:  # Mover Abajo
            movimientos.append((self.fila + 1, self.columna))    
        if self.columna < len(matriz[0]) - 1 and matriz[self.fila][self.columna + 1] != 1:  # Mover Derecha
            movimientos.append((self.fila, self.columna + 1))   

        return movimientos

    def generar_nodo(self):
        estado = (self.fila, self.columna)  # Estado del Mando
        return Nodo(estado)
