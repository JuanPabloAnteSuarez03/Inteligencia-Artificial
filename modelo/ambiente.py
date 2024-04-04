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
ambiente.cargar_desde_archivo('C:/Users/nicol/OneDrive/Escritorio/inteligencia/Inteligencia-Artificial/modelo/ambiente.txt')
ambiente.mostrar_ambiente()


nave = ambiente.naves
grogu = ambiente.grogu
manda = ambiente.mando
enemigos = ambiente.enemigos

enemigo1 = enemigos[0]
enemigo2 = enemigos[1]
enemigo3 = enemigos[2]
enemigo4 = enemigos[3]
enemigo5 = enemigos[4]

nave1 = nave[0]



print ( "nave", nave1.get_posicion())
print ( "grogu", grogu.get_posicion())
print ( "mando", manda.get_posicion())
print ( "enemigo 1", enemigo1.get_posicion())
print ( "enemigo 2", enemigo2.get_posicion())
print ( "enemigo 3", enemigo3.get_posicion())
print ( "enemigo 4", enemigo4.get_posicion())
print ( "enemigo 5", enemigo5.get_posicion())




