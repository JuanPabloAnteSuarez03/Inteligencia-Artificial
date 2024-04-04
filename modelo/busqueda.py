import time
from ambiente import *
from arbol import *

def busqueda_preferente_por_profundidad(problema):
    pila = [Nodo(problema)]
    
    while pila:
        if not pila:
            return "Falla"
        
        n = pila.pop()
        
        if es_nodo_meta(n):
            return "Solución encontrada"
        
        # Expansión del nodo y agregar todos sus hijos a la pila
        hijos = expandir_nodo(n)
        for hijo in hijos:
            pila.append(hijo)
    
    return "Falla"



# Ejemplo de uso:
ambiente = Ambiente()  # Crear un ambiente
ambiente.cargar_desde_archivo(r'modelo\ambientebasico.txt')  # Cargar el ambiente desde un archivo
ambiente.asignar_objetos()  # Asignar los objetos en el ambiente

# Suponiendo que queremos encontrar un camino desde la posición actual del Mando hasta Grogu
camino = dfs(ambiente, ambiente.mando, ambiente.grogu)
print(camino)

if camino[0]:
    print("Camino encontrado:")
    for paso in camino:
        print(paso)
else:
    print("No se encontró un camino hacia el objetivo.")

