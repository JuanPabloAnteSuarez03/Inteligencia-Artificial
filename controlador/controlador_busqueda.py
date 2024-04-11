from queue import PriorityQueue
from busqueda import busqueda_profundidad, busqueda_amplitud, busqueda_costo_uniforme

def busqueda_controlador(ambiente, metodo_busqueda):
    inicio = time.time()
    if metodo_busqueda == "profundidad":
        camino, mensaje, nodos_expandidos, profundidad, tiempo_total = busqueda_profundidad(ambiente)
    elif metodo_busqueda == "amplitud":
        camino, mensaje, nodos_expandidos, profundidad, tiempo_total = busqueda_amplitud(ambiente)
    elif metodo_busqueda == "costo_uniforme":
        camino, mensaje, nodos_expandidos, profundidad, tiempo_total, costo_total = busqueda_costo_uniforme(ambiente)
    else:
        return [], "Método de búsqueda no válido", [], 0, 0
    
    return camino, mensaje, len(nodos_expandidos), tiempo_total, profundidad, costo_total if metodo_busqueda == "costo_uniforme" else tiempo_total
