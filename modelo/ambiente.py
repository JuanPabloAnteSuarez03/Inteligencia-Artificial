from busqueda import Busqueda

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
        self.matriz[self.mando.fila][self.mando.columna] = 0
        self.matriz[nueva_fila][nueva_columna] = 2
        self.mando.fila = nueva_fila
        self.mando.columna = nueva_columna
    
    def buscar_solucion(self, estado_inicial, objetivo):
        encontrado, nodos_expandidos, profundidad, tiempo = Busqueda.busqueda_amplitud(estado_inicial, objetivo)
        if encontrado:
            print("Solución encontrada!")
            print("Cantidad de nodos expandidos:", nodos_expandidos)
            print("Profundidad del árbol:", profundidad)
            print("Tiempo de cómputo:", tiempo, "segundos")
        else:
            print("No se encontró solución.")
