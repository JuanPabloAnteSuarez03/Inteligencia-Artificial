from nave import *
from enemigo import *
from grogu import *
from mando import *
from arbol import *

class Ambiente:
    def __init__(self):
        self.matriz = [[0] * 10 for _ in range(10)]
        self.mando = None
        self.grogu = None
        self.naves = []
        self.enemigos = []  
        
    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as file:
            self.matriz = [[int(x) for x in line.split()] for line in file.readlines()]

    def asignar_objetos(self):
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
    
    def copy(self):
        copia = Ambiente()
        copia.matriz = [fila[:] for fila in self.matriz]
        copia.mando = Mando(self.mando.fila, self.mando.columna) if self.mando else None
        copia.grogu = Grogu(self.grogu.fila, self.grogu.columna) if self.grogu else None
        copia.naves = [Nave(nave.fila, nave.columna) for nave in self.naves]
        copia.enemigos = [Enemigo(enemigo.fila, enemigo.columna) for enemigo in self.enemigos]
        return copia

    def get_casilla(self, fila, columna):
        return self.matriz[fila][columna]
    
    def mostrar_ambiente(self):
        for fila in self.matriz:
            print(' '.join(map(str, fila)))

    def transicion(self, accion):
        nueva_fila, nueva_columna = accion[0], accion[1]
        self.matriz[self.mando.fila][self.mando.columna] = 0  # Limpiar la posición anterior del Mando
        self.matriz[nueva_fila][nueva_columna] = 2  # Colocar al Mando en la nueva posición
        self.mando.fila = nueva_fila  # Actualizar la fila del Mando
        self.mando.columna = nueva_columna  # Actualizar la columna del Mando

    
# # Ejemplo de uso
# ambiente = Ambiente()
# ambiente.cargar_desde_archivo(r'modelo\ambientebasico.txt')
# ambiente.asignar_objetos()
# ambiente.mostrar_ambiente()
# print()
# # Suponiendo que ya has creado un objeto de la clase Ambiente llamado "ambiente"

# # Obtenemos los movimientos posibles para el Mando en la posición actual
# movimientos_posibles = ambiente.mando.get_movimientos_posibles(ambiente.matriz)

# # Supongamos que queremos mover al Mando hacia arriba, y esa acción está en la lista de movimientos posibles
# accion = movimientos_posibles[0]  # Por ejemplo, el primer movimiento posible

# # Aplicamos la acción y obtenemos un nuevo estado del ambiente
# ambiente.transicion(accion)
# print(type(ambiente.grogu))
# # Ahora podemos verificar el estado del nuevo ambiente
# ambiente.mostrar_ambiente()


# nave = ambiente.naves
# grogu = ambiente.grogu
# manda = ambiente.mando
# enemigos = ambiente.enemigos

# enemigo1 = enemigos[0]
# enemigo2 = enemigos[1]
# enemigo3 = enemigos[2]
# enemigo4 = enemigos[3]
# enemigo5 = enemigos[4]

# nave1 = nave[0]
# mando1 = ambiente.mando
# print ( "nave", nave1.get_posicion())
# print ( "grogu", grogu.get_posicion())
# print ( "mando", manda.get_posicion())
# print ( "enemigo 1", enemigo1.get_posicion())
# print ( "enemigo 2", enemigo2.get_posicion())
# print ( "enemigo 3", enemigo3.get_posicion())
# print ( "enemigo 4", enemigo4.get_posicion())
# print ( "enemigo 5", enemigo5.get_posicion())




