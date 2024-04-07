import time
from ambiente import *
from arbol import *

def es_nodo_meta(nodo, objetivo):
    ambiente1 = nodo.estado
    mando1 = ambiente1.mando
    posicion_mando = mando1.get_posicion()  # Obtener la posición actual del Mando
    posicion_objetivo = (objetivo.fila, objetivo.columna)  # Obtener la posición objetivo (Grogu)
    
    # Verificar si la posición del Mando coincide con la posición objetivo
    return posicion_mando == posicion_objetivo

def evitar_ciclo(nodo):
    if nodo.profundidad <= 1:
        return False
    antecesor = nodo.padre.padre
    
    while(antecesor != None):
        if antecesor.estado == nodo.estado:
            return True
        antecesor = antecesor.padre

    return False

def reconstruir_camino(nodo):
    camino = []
    while nodo.padre is not None:
        camino.append(nodo.operador)
        nodo = nodo.padre
    camino.reverse()  # Invertir el camino para obtener el orden correcto
    return camino

 
def busqueda_preferente_por_profundidad(problema):
    pila = [Nodo(problema)]
    nodos_visitados = []

    while pila:

        n = pila.pop()
        profundidad_actual = n.profundidad
        grogu = problema.grogu
        if es_nodo_meta(n, grogu):
            return reconstruir_camino(n), "Se encontró"
        
        # Expansión del nodo y agregar todos sus hijos a la pila
        movimientos_posibles = n.estado.mando.get_movimientos_posibles(n.estado.matriz)
        print(movimientos_posibles)
        for movimiento in movimientos_posibles:
            padre = n
            nueva_fila, nueva_columna = movimiento
            n.estado.transicion((nueva_fila, nueva_columna))
            #n.estado.mostrar_ambiente()
            if evitar_ciclo(n):
                print("evite un ciclo :)")
                continue
            nuevo_nodo = Nodo(n.estado, padre, movimiento, profundidad_actual + 1)
            nodos_visitados.append(nuevo_nodo)
            pila.append(nuevo_nodo)
            print(reconstruir_camino(n))
    return "Falla"

# Definir el problema
ambiente = Ambiente()
ambiente.cargar_desde_archivo(r'modelo\ambientebasico.txt')
ambiente.asignar_objetos()
print(busqueda_preferente_por_profundidad(ambiente))