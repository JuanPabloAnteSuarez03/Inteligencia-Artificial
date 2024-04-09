import time
from ambiente import *
from arbol import *

def es_nodo_meta(nodo):
    ambiente = nodo.estado
    mando_posicion = ambiente.mando.get_posicion()
    grogu_posicion = ambiente.grogu.get_posicion()
    
    # Verificar si la posición del Mando coincide con la posición de Grogu
    return mando_posicion == grogu_posicion

def reconstruir_camino(nodo):
    camino = []
    while nodo.padre is not None:
        camino.append(nodo.operador)
        nodo = nodo.padre
    camino.reverse()  # Invertir el camino para obtener el orden correcto
    return camino

def evitar_ciclo(nodo):
    if nodo.profundidad <= 1:
        return False
    antecesor = nodo.padre.padre

    while antecesor is not None:
        if antecesor.estado == nodo.estado:
            return True
        antecesor = antecesor.padre

    return False

def busqueda_dfs(ambiente):
    nodo = Nodo(ambiente)
    stack = [nodo]  # Usar una pila para almacenar nodos a explorar
    
    while stack:
        nodo_actual = stack.pop()  # Obtener el nodo más reciente de la pila
        
        if es_nodo_meta(nodo_actual):
            return reconstruir_camino(nodo_actual), "Se encontró"
        
        if nodo_actual.profundidad >= 100:  # Evitar bucles infinitos
            continue
        
        for accion in nodo_actual.estado.mando.get_movimientos_posibles(nodo_actual.estado.matriz):
            nuevo_estado = nodo_actual.estado.copy()
            nuevo_estado.transicion(accion)
            nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, nodo_actual.profundidad + 1)
            
            if not evitar_ciclo(nuevo_nodo):
                stack.append(nuevo_nodo)  # Agregar el nuevo nodo a la pila
    
    return [], "No se encontró"

# Cargar el ambiente desde el archivo
ambiente = Ambiente()
ambiente.cargar_desde_archivo(r'modelo\ambientebasico.txt')

# Realizar la búsqueda DFS
inicio = time.time()
camino, mensaje = busqueda_dfs(ambiente)
tiempo_total = time.time() - inicio

print("Camino encontrado:", camino)
print("Mensaje:", mensaje)
print("Tiempo de ejecución:", tiempo_total)