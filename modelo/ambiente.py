from nave import *
from enemigo import *
from grogu import *
from mando import *

class Ambiente:
    def __init__(self):
        self.matriz = [[0] * 10 for _ in range(10)]
        self.matriz = None
        self.mando = None
        self.grogu = None
        self.naves = []
        self.enemigos = []  
        
    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as file:
            self.matriz = [[int(x) for x in line.split()] for line in file.readlines()]
        
        for fila_index, fila in enumerate(self.matriz):
            for columna_index, valor in enumerate(fila):
                if valor == 2:  # Mando
                    self.mando = Mando(fila_index, columna_index)
                elif valor == 5:  # Grogu
                    self.grogu = Grogu(fila_index, columna_index)
                elif valor == 3:  # Nave
                    self.naves.append(Nave(fila_index, columna_index))
                elif valor == 4:  # Enemigo
                    self.enemigos.append(Enemigo(fila_index, columna_index))
    
    def get_casilla(self, fila, columna):
        return self.matriz[fila][columna]
    
    def mostrar_ambiente(self):
        for fila in self.matriz:
            print(' '.join(map(str, fila)))

    def get_matriz(self):
        return self.matriz
    
    def get_mando(self):
        return self.mando
    
    def get_grogu(self):
        return self.grogu
    
    def get_naves(self):
        return self.naves
    
    def get_enemigos(self):
        return self.enemigos    

# Ejemplo de uso
ambiente = Ambiente()
ambiente.cargar_desde_archivo('C:/Users/jpant/OneDrive/Desktop/Universidad/Inteligencia Artificial/modelo/ambiente.txt')
ambiente.mostrar_ambiente()
