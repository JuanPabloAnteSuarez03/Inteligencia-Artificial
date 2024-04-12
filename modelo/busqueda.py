import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'vista'))

import tkinter as tk
from tkinter import messagebox
import time

from cuadricula import *

from ambiente import *
from arbol import *
from collections import deque
from queue import PriorityQueue



def es_nodo_meta(nodo):
    ambiente = nodo.estado
    mando_posicion = ambiente.mando.get_posicion()
    grogu_posicion = ambiente.grogu.get_posicion()
    
    # Verificar si la posición del Mando coincide con la posición de Grogu
    return mando_posicion == grogu_posicion

def es_enemigo(nodo):
    ambiente = nodo.estado
    mando_posicion = ambiente.mando.get_posicion()
    enemigos = ambiente.enemigos
    for enemigo in enemigos:
        if enemigo.get_posicion() == mando_posicion:
            return True
    return False            

def es_nave(nodo):
    if nodo.paso_por_nave:
        return True
    else:
        ambiente = nodo.estado
        mando_posicion = ambiente.mando.get_posicion()
        naves = ambiente.naves
        for nave in naves:
            if nave.get_posicion() == mando_posicion:
                return True
        return False  

def reconstruir_camino(nodo):
    camino = []
    while nodo.padre is not None:
        camino.append(nodo.operador)
        nodo = nodo.padre
    camino.reverse()  # Invertir el camino para obtener el orden correcto
    return camino

def evitar_ciclos(nodo):
    if nodo.profundidad <= 1:
        return False
    antecesor = nodo.padre.padre

    while antecesor is not None:
        if antecesor.estado == nodo.estado:
            return True
        antecesor = antecesor.padre

    return False

def busqueda_profundidad(ambiente):
    inicio = time.time()
    nodo = Nodo(ambiente)
    stack = [nodo]  # Usar una pila para almacenar nodos a explorar
    explorados = set()  # Conjunto para almacenar estados explorados
    nodos_expandidos = []  # Lista para almacenar los nodos expandidos
    
    while stack:
        nodo_actual = stack.pop()  # Obtener el nodo más reciente de la pila
        
        if es_nodo_meta(nodo_actual):
            tiempo_total = time.time() - inicio
            return reconstruir_camino(nodo_actual), "Se encontró", nodos_expandidos, nodo_actual.profundidad, tiempo_total
         
        estado_actual = str(nodo_actual.estado.matriz)  # Convertir la matriz a una cadena para usarla como clave
        
        if estado_actual in explorados or evitar_ciclos(nodo_actual):
            continue  # Evitar nodos ya explorados y ciclos
        
        explorados.add(estado_actual)  # Agregar el estado actual al conjunto de explorados
        nodos_expandidos.append(nodo_actual)  # Agregar el nodo actual a la lista de nodos expandidos
        
        for accion in nodo_actual.estado.mando.get_movimientos_posibles(nodo_actual.estado.matriz):
            nuevo_estado = nodo_actual.estado.copy()
            nuevo_estado.transicion(accion)
            nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1)
            stack.append(nuevo_nodo)  # Agregar el nuevo nodo a la pila
    
    return [], "No se encontró", nodos_expandidos




def busqueda_amplitud(ambiente):
    inicio = time.time()
    nodo = Nodo(ambiente)
    queue = deque([nodo])  # Usar una cola para almacenar nodos a explorar
    explorados = set()  # Conjunto para almacenar estados explorados
    nodos_expandidos = []  # Lista para almacenar los nodos expandidos 
    while queue:
        nodo_actual = queue.popleft()  # Obtener el nodo más antiguo de la cola
        
        if es_nodo_meta(nodo_actual):
            tiempo_total = time.time() - inicio
            return reconstruir_camino(nodo_actual), "Se encontró", nodos_expandidos, nodo_actual.profundidad, tiempo_total
         
        estado_actual = str(nodo_actual.estado.matriz)  # Convertir la matriz a una cadena para usarla como clave
        
        if estado_actual in explorados or evitar_ciclos(nodo_actual):
            continue  # Evitar nodos ya explorados y ciclos
        
        explorados.add(estado_actual)  # Agregar el estado actual al conjunto de explorados
        nodos_expandidos.append(nodo_actual)  # Agregar el nodo actual a la lista de nodos expandidos
        
        for accion in nodo_actual.estado.mando.get_movimientos_posibles(nodo_actual.estado.matriz):
            nuevo_estado = nodo_actual.estado.copy()
            nuevo_estado.transicion(accion)
            nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1)
            queue.append(nuevo_nodo)  # Agregar el nuevo nodo a la cola
    
    return [], "No se encontró", nodos_expandidos




def busqueda_costo_uniforme(ambiente):
    inicio = time.time()
    nodo = Nodo(ambiente)
    queue = PriorityQueue()  # Usar una cola de prioridad para almacenar nodos a explorar
    queue.put((nodo.costo, nodo))  # Insertar el nodo inicial en la cola de prioridad
    explorados = set()  # Conjunto para almacenar estados explorados
    nodos_expandidos = []  # Lista para almacenar los nodos expandidos 
    
    while not queue.empty():
        _, nodo_actual = queue.get()  # Obtener el nodo con el menor costo acumulado de la cola de prioridad
        
        if es_nodo_meta(nodo_actual):
            tiempo_total = time.time() - inicio
            return reconstruir_camino(nodo_actual), "Se encontró", nodos_expandidos, nodo_actual.profundidad, tiempo_total, nodo_actual.costo
         
        estado_actual = str(nodo_actual.estado.matriz)  # Convertir la matriz a una cadena para usarla como clave
        
        if estado_actual in explorados or evitar_ciclos(nodo_actual):
            continue  # Evitar nodos ya explorados y ciclos
        
        explorados.add(estado_actual)  # Agregar el estado actual al conjunto de explorados
        nodos_expandidos.append(nodo_actual)  # Agregar el nodo actual a la lista de nodos expandidos
        
        for accion in nodo_actual.estado.mando.get_movimientos_posibles(nodo_actual.estado.matriz):
            nuevo_estado = nodo_actual.estado.copy()
            nuevo_estado.transicion(accion)
            if es_nave(nodo_actual) and not es_enemigo(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 1/2, nodo_actual.contador_pasos + 1, True, nodo_actual.paso_por_enemigo)
                if nuevo_nodo.contador_pasos >= 10:
                    nuevo_nodo.paso_por_nave = False
                    nuevo_nodo.contador_pasos = 0

            if es_nave(nodo_actual) and es_enemigo(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 1/2, nodo_actual.contador_pasos, nodo_actual.paso_por_nave, nodo_actual.paso_por_enemigo)
            elif es_enemigo(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 5, nodo_actual.contador_pasos, nodo_actual.paso_por_nave, nodo_actual.paso_por_enemigo)
            if not es_enemigo(nodo_actual) and not es_nave(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 1, nodo_actual.contador_pasos, nodo_actual.paso_por_nave, nodo_actual.paso_por_enemigo)
            queue.put((nuevo_nodo.costo, nuevo_nodo))  # Agregar el nuevo nodo a la cola de prioridad
    
    return [], "No se encontró", nodos_expandidos


def heuristica(nodo):
    distancia_manhattan_mando_grogu = abs(nodo.estado.mando.fila - nodo.estado.grogu.fila) + abs(nodo.estado.mando.columna - nodo.estado.grogu.columna)
    naves = nodo.estado.naves
    enemigos = nodo.estado.enemigos
    
    if naves or enemigos:
        distancias_nave_grogu = []
        distancias_nave_mando = []
        for nave in naves:
            distancia_manhattan_nave_grogu = abs(nave.fila - nodo.estado.grogu.fila) + abs(nave.columna - nodo.estado.grogu.columna)
            distancia_manhattan_nave_mando = abs(nave.fila - nodo.estado.mando.fila) + abs(nave.columna - nodo.estado.mando.columna)
            distancias_nave_grogu.append(distancia_manhattan_nave_grogu)
            distancias_nave_mando.append(distancia_manhattan_nave_mando)
        
        distancia_desde_nave = min(distancias_nave_mando) + min(distancias_nave_grogu)
        
        if min(distancias_nave_grogu) <= 5:
            distancia_desde_nave -= 5
        
        # Penalizar si el Mando está en una posición ocupada por un enemigo
        mando_posicion = nodo.estado.mando.get_posicion()
        for enemigo in enemigos:
            if enemigo.get_posicion() == mando_posicion:
                distancia_desde_nave += 10
        
        return distancia_desde_nave
    
    return distancia_manhattan_mando_grogu


def busqueda_avara(ambiente):
    inicio = time.time()
    nodo = Nodo(ambiente)
    queue = PriorityQueue()  # Usar una cola de prioridad para almacenar nodos a explorar
    queue.put((heuristica(nodo), nodo))  # Insertar el nodo inicial en la cola de prioridad
    
    explorados = set()  # Conjunto para almacenar estados explorados
    nodos_expandidos = []  # Lista para almacenar los nodos expandidos 
    
    while not queue.empty():
        _, nodo_actual = queue.get()  # Obtener el nodo con la menor heurística de la cola
        
        if es_nodo_meta(nodo_actual):
            tiempo_total = time.time() - inicio
            return reconstruir_camino(nodo_actual), "Se encontró", nodos_expandidos, nodo_actual.profundidad, tiempo_total, nodo_actual.costo
         
        estado_actual = str(nodo_actual.estado.matriz)  # Convertir la matriz a una cadena para usarla como clave
        
        if estado_actual in explorados or evitar_ciclos(nodo_actual):
            continue  # Evitar nodos ya explorados y ciclos
        
        explorados.add(estado_actual)  # Agregar el estado actual al conjunto de explorados
        nodos_expandidos.append(nodo_actual)  # Agregar el nodo actual a la lista de nodos expandidos
        
        for accion in nodo_actual.estado.mando.get_movimientos_posibles(nodo_actual.estado.matriz):
            nuevo_estado = nodo_actual.estado.copy()
            nuevo_estado.transicion(accion)
            if es_nave(nodo_actual) and not es_enemigo(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 1/2, nodo_actual.contador_pasos + 1, True, nodo_actual.paso_por_enemigo)
                if nuevo_nodo.contador_pasos >= 10:
                    nuevo_nodo.paso_por_nave = False
                    nuevo_nodo.contador_pasos = 0

            if es_nave(nodo_actual) and es_enemigo(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 1/2, nodo_actual.contador_pasos, nodo_actual.paso_por_nave, nodo_actual.paso_por_enemigo)
            elif es_enemigo(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 5, nodo_actual.contador_pasos, nodo_actual.paso_por_nave, nodo_actual.paso_por_enemigo)
            if not es_enemigo(nodo_actual) and not es_nave(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 1, nodo_actual.contador_pasos, nodo_actual.paso_por_nave, nodo_actual.paso_por_enemigo)
            queue.put((heuristica(nuevo_nodo), nuevo_nodo))  # Insertar el nuevo nodo en la cola de prioridad
    
    return [], "No se encontró", nodos_expandidos

def a_estrella(ambiente):
    inicio = time.time()
    nodo = Nodo(ambiente)
    queue = PriorityQueue()  # Usar una cola de prioridad para almacenar nodos a explorar
    queue.put((0, nodo))  # Insertar el nodo inicial en la cola de prioridad con costo 0
    
    explorados = set()  # Conjunto para almacenar estados explorados
    nodos_expandidos = []  # Lista para almacenar los nodos expandidos 
    
    while not queue.empty():
        _, nodo_actual = queue.get()  # Obtener el nodo con el menor costo de la cola
        
        if es_nodo_meta(nodo_actual):
            tiempo_total = time.time() - inicio
            return reconstruir_camino(nodo_actual), "Se encontró", nodos_expandidos, nodo_actual.profundidad, tiempo_total, nodo_actual.costo
         
        estado_actual = str(nodo_actual.estado.matriz)  # Convertir la matriz a una cadena para usarla como clave
        
        if estado_actual in explorados or evitar_ciclos(nodo_actual):
            continue  # Evitar nodos ya explorados y ciclos
        
        explorados.add(estado_actual)  # Agregar el estado actual al conjunto de explorados
        nodos_expandidos.append(nodo_actual)  # Agregar el nodo actual a la lista de nodos expandidos
        
        for accion in nodo_actual.estado.mando.get_movimientos_posibles(nodo_actual.estado.matriz):
            nuevo_estado = nodo_actual.estado.copy()
            nuevo_estado.transicion(accion)
            if es_nave(nodo_actual) and not es_enemigo(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 1/2, nodo_actual.contador_pasos + 1, True, nodo_actual.paso_por_enemigo)
                if nuevo_nodo.contador_pasos >= 10:
                    nuevo_nodo.paso_por_nave = False
                    nuevo_nodo.contador_pasos = 0

            if es_nave(nodo_actual) and es_enemigo(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 1/2, nodo_actual.contador_pasos, nodo_actual.paso_por_nave, nodo_actual.paso_por_enemigo)
            elif es_enemigo(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 5, nodo_actual.contador_pasos, nodo_actual.paso_por_nave, nodo_actual.paso_por_enemigo)
            if not es_enemigo(nodo_actual) and not es_nave(nodo_actual):
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1, nodo_actual.costo + 1, nodo_actual.contador_pasos, nodo_actual.paso_por_nave, nodo_actual.paso_por_enemigo)
            
            # Calcular el costo acumulado desde el nodo inicial hasta el nodo actual
            costo_acumulado = nodo_actual.costo + 1
            
            # Calcular la heurística desde el nodo actual hasta el nodo objetivo
            heuristica_estimada = heuristica(nuevo_nodo)
            
            # Calcular el costo total del nuevo nodo
            costo_total = costo_acumulado + heuristica_estimada
            print(costo_total)
            queue.put((costo_total, nuevo_nodo))  # Insertar el nuevo nodo en la cola de prioridad
    
    return [], "No se encontró", nodos_expandidos


ambiente = Ambiente()
ambiente.cargar_desde_archivo(r'modelo\ambiente.txt')
ambiente.asignar_objetos()

# Obtenemos los movimientos posibles para el Mando en la posición actual
movimientos_posibles = ambiente.mando.get_movimientos_posibles(ambiente.matriz)

# Supongamos que queremos mover al Mando hacia arriba, y esa acción está en la lista de movimientos posibles
accion = movimientos_posibles[0]  # Por ejemplo, el primer movimiento posible

# Aplicamos la acción y obtenemos un nuevo estado del ambiente
movimientos, mensaje, nodos_expandidos, profundidad, tiempo  = busqueda_amplitud(ambiente)


def ejecutar_busqueda_y_mostrar_cuadricula(ambiente, movimientos):
    # Crear una instancia de la clase Cuadricula
    root = tk.Tk()
    cuadricula = Cuadricula(root, width=500, height=500)

    # Llama al método para actualizar el lienzo con la nueva matriz del ambiente
    cuadricula.actualizar_canvas(ambiente.matriz)

    for movimiento in movimientos:
        ambiente.transicion(movimiento)
        ambiente.mostrar_ambiente()
        cuadricula.actualizar_canvas(ambiente.matriz)
        root.update()
        time.sleep(0.5)

    root.mainloop()


# # Suponiendo que ya has creado un objeto de la clase Ambiente llamado "ambiente"

# # Obtenemos los movimientos posibles para el Mando en la posición actual
# movimientos_posibles = ambiente.mando.get_movimientos_posibles(ambiente.matriz)

# # Supongamos que queremos mover al Mando hacia arriba, y esa acción está en la lista de movimientos posibles
# accion = movimientos_posibles[0]  # Por ejemplo, el primer movimiento posible

# # Aplicamos la acción y obtenemos un nuevo estado del ambiente
# movimientos, mensaje, nodos_expandidos, profundidad, tiempo  = busqueda_amplitud(ambiente)
# for movimiento in movimientos:
#     ambiente.transicion(movimiento)
#     ambiente.mostrar_ambiente()
#     print()
# Ahora podemos verificar el estado del nuevo ambiente
# Cargar el ambiente desde el archivo
#ambiente = Ambiente()
#ambiente.cargar_desde_archivo(r'modelo\ambiente.txt')
print(heuristica(Nodo(ambiente)))

# Realizar la búsqueda DFS
camino, mensaje, nodos_expandidos, profundidad , tiempo_total, costo = busqueda_avara(ambiente)  # Modifica esta línea

print("Camino encontrado:", camino)
print("Mensaje:", mensaje)
print("Nodos expandidos:", len(nodos_expandidos))  # Agrega esta línea para mostrar los nodos expandidos
print("Tiempo de ejecución:", tiempo_total)
print("Profundidad:", profundidad)
print("Costo", costo)
