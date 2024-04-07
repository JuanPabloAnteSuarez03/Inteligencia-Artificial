class Nodo:
    def __init__(self, estado, padre=None, operador=None, profundidad=0, costo=0):
        self.estado = estado            # Estado del problema en este nodo
        self.padre = padre              # Referencia al nodo padre
        self.operador = operador        # Operador aplicado para generar este nodo
        self.profundidad = profundidad  # Profundidad del nodo en el árbol
        self.costo = costo              # Costo de la ruta desde la raíz hasta este nodo
        self.hijos = []                 # Lista de nodos hijos

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

# A = "A"
# B = "B"
# C = "C"

# # Ejemplo de cómo crear nodos y agregar hijos
# nodo_raiz = Nodo(A)  # Suponiendo que 'estado_raiz' es el estado inicial del problema
# nodo_hijo1 = Nodo(B, padre=nodo_raiz, operador="Operador1", profundidad=1, costo=10)
# nodo_hijo2 = Nodo(C, padre=nodo_raiz, operador="Operador2", profundidad=1, costo=15)

# nodo_raiz.agregar_hijo(nodo_hijo1)
# nodo_raiz.agregar_hijo(nodo_hijo2)

# hijo1 = nodo_hijo1.padre.hijos[0]
# hijo2 = nodo_hijo1.padre.hijos[1]

# print(hijo1.estado, hijo2.estado)