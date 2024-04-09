import time
from collections import deque

class Estado:
    def __init__(self, fila, columna, en_nave=False, costo=0, camino=None, combustible=10):
        self.fila = fila
        self.columna = columna
        self.en_nave = en_nave
        self.costo = costo
        self.camino = camino if camino is not None else [(fila, columna)]
        self.combustible = combustible

class Ambiente:
    def __init__(self, archivo_ambiente):
        self.matriz, self.grogu, self.naves = self.cargar_desde_archivo(archivo_ambiente)

    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as file:
            lines = file.readlines()
            matriz = [[int(x) for x in line.split()] for line in lines]
            grogu = None
            naves = []
            for i, row in enumerate(matriz):
                for j, cell in enumerate(row):
                    if cell == 2:  # aqui inicia  Grogu
                        grogu = (i, j)
                    elif cell == 3:  # Nave
                        naves.append((i, j))
            return matriz, grogu, naves

def bfs(ambiente):
    inicio = ambiente.grogu
    frontera = deque([Estado(inicio[0], inicio[1])])
    visitados = set()
    nodos_expandidos = 0
    profundidad_max = 0
    inicio_tiempo = time.time()

    while frontera:
        estado_actual = frontera.popleft()
        nodos_expandidos += 1
        profundidad_max = max(profundidad_max, estado_actual.costo)

        if ambiente.matriz[estado_actual.fila][estado_actual.columna] == 5:  # Grogu encontrado
            fin_tiempo = time.time()
            tiempo_transcurrido = fin_tiempo - inicio_tiempo
            return estado_actual, nodos_expandidos, profundidad_max, tiempo_transcurrido

        visitados.add((estado_actual.fila, estado_actual.columna))

        for accion in acciones_posibles(ambiente, estado_actual):
            nueva_fila, nueva_columna, nuevo_en_nave, nuevo_costo, nuevo_combustible = accion
            nuevo_camino = estado_actual.camino + [(nueva_fila, nueva_columna)]
            nuevo_estado = Estado(nueva_fila, nueva_columna, nuevo_en_nave, estado_actual.costo + nuevo_costo, nuevo_camino, nuevo_combustible)
            if (nuevo_estado.fila, nuevo_estado.columna) not in visitados:
                frontera.append(nuevo_estado)

    return None, nodos_expandidos, profundidad_max, None

def acciones_posibles(ambiente, estado):
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    acciones = []
    for movimiento in movimientos:
        nueva_fila = estado.fila + movimiento[0]
        nueva_columna = estado.columna + movimiento[1]

        if 0 <= nueva_fila < len(ambiente.matriz) and 0 <= nueva_columna < len(ambiente.matriz[0]):
            if ambiente.matriz[nueva_fila][nueva_columna] != 1:
                costo_movimiento = 1
                en_nave = estado.en_nave
                combustible = estado.combustible

                if ambiente.matriz[nueva_fila][nueva_columna] == 3:  # Si la casilla es la nave
                    if estado.en_nave:  # si esta en la nave, costo de movimiento normal y reducir combustible
                        costo_movimiento = 0.5
                        combustible -= 1
                    else:  # Si no está en la nave, reducir costo y marcar que está en la nave
                        costo_movimiento = 1
                        en_nave = True

                if ambiente.matriz[nueva_fila][nueva_columna] == 4:  # Si la casilla es un enemigo
                    if estado.en_nave:  # Si está en la nave, puede pasar sin daño
                        costo_movimiento = 0.5
                    else:  # Si no está en la nave, incrementar el costo y reducir combustible
                        costo_movimiento = 5
                        combustible -= 1

                acciones.append((nueva_fila, nueva_columna, en_nave, costo_movimiento, combustible))

    return acciones

def imprimir_reporte(resultado, nodos_expandidos, profundidad_max, tiempo_transcurrido):
    if resultado:
        estado_final, nodos_exp, prof_max, tiempo = resultado
        print("Grogu encontrado en la posición:", estado_final.fila, estado_final.columna)
        print("Camino recorrido:", estado_final.camino)
        print("Costo de la solución:", estado_final.costo)
    else:
        print("Grogu no fue encontrado.")

    print("Cantidad de nodos expandidos:", nodos_expandidos)
    print("Profundidad máxima del árbol:", profundidad_max)
    print("Tiempo de cómputo:", tiempo_transcurrido, "segundos")

# Ejemplo de uso
archivo_ambiente = "./ambiente.txt"
ambiente = Ambiente(archivo_ambiente)

# Realizar búsqueda por amplitud
resultado_bfs = bfs(ambiente)

# Imprimir reporte de búsqueda por amplitud
imprimir_reporte(resultado_bfs, *resultado_bfs[1:])
