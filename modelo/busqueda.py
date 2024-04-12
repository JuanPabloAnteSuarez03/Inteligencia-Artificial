import time
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
    mando_posicion = nodo.estado.mando.get_posicion()
    grogu_posicion = nodo.estado.grogu.get_posicion()
    
    # Obtener los movimientos posibles del Mando
    movimientos_posibles = nodo.estado.mando.get_movimientos_posibles(nodo.estado.matriz)
    
    # Inicializar una lista para almacenar las distancias al objetivo desde cada movimiento posible
    distancias = []
    
    # Calcular la distancia al objetivo desde cada movimiento posible
    for movimiento in movimientos_posibles:
        # Copiar el estado actual para simular el movimiento del Mando
        nuevo_estado = nodo.estado.copy()
        nuevo_estado.mando.set_posicion(*movimiento)
        
        # Verificar si el movimiento es sobre un enemigo
        if nuevo_estado.matriz[movimiento[0]][movimiento[1]] == 4:
            # Si es enemigo, agregar una penalización a la distancia
            distancia_manhattan = abs(movimiento[0] - grogu_posicion[0]) + abs(movimiento[1] - grogu_posicion[1])
            distancia_manhattan += 5
        else:
            # Calcular la distancia manhattan desde este movimiento al objetivo
            distancia_manhattan = abs(movimiento[0] - grogu_posicion[0]) + abs(movimiento[1] - grogu_posicion[1])
            
            # Si en el movimiento hay una nave, dividir la distancia por 2
            if nuevo_estado.matriz[movimiento[0]][movimiento[1]] == 3:
                distancia_manhattan /= 2
        
        distancias.append(distancia_manhattan)
    
    # Devolver la mínima distancia al objetivo
    return min(distancias)





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
            queue.put((heuristica(nuevo_nodo), nuevo_nodo))  # Insertar el nuevo nodo en la cola de prioridad
    
    return [], "No se encontró", nodos_expandidos


# Ejemplo de uso
ambiente = Ambiente()
ambiente.cargar_desde_archivo(r'modelo\ambiente.txt')
ambiente.asignar_objetos()
# Suponiendo que ya has creado un objeto de la clase Ambiente llamado "ambiente"

# Obtenemos los movimientos posibles para el Mando en la posición actual
movimientos_posibles = ambiente.mando.get_movimientos_posibles(ambiente.matriz)

# Supongamos que queremos mover al Mando hacia arriba, y esa acción está en la lista de movimientos posibles
accion = movimientos_posibles[0]  # Por ejemplo, el primer movimiento posible

# Aplicamos la acción y obtenemos un nuevo estado del ambiente
movimientos, mensaje, nodos_expandidos, profundidad, tiempo  = busqueda_amplitud(ambiente)


image_paths = {
        1: "imagenes/negro.png",
        2: "imagenes/mandalorian.png",
        3: "imagenes/nave.png",
        4: "imagenes/darthVader.png",
        5: "imagenes/grogu.png",
        6: "imagenes/mandalorian_y_grogu.png"
    }



import tkinter as tk
import time

class PacmanGUI:
    def __init__(self, root, matrix_size):
        self.root = root
        self.matrix_size = matrix_size
        self.canvas = tk.Canvas(root, width=matrix_size*30, height=matrix_size*30, bg='black')
        self.canvas.pack()
        self.images = {}  # Un diccionario para almacenar las imágenes cargadas
        self.load_images()  # Carga las imágenes
        self.draw_matrix([[0]*matrix_size]*matrix_size)

    def load_images(self):
        # Carga las imágenes desde las rutas proporcionadas y almacénalas en el diccionario self.images
        for key, path in image_paths.items():
            self.images[key] = tk.PhotoImage(file=path)

    def draw_matrix(self, matrix):
        self.canvas.delete("all")
        cell_size = 30
        image_padding = 2  # Ajusta este valor según sea necesario para el espaciado deseado

    def draw_matrix(self, matrix):
        self.canvas.delete("all")
        cell_size = 30

        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                x0, y0 = j * cell_size, i * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size
                if matrix[i][j] in self.images:
                    # Obtiene la imagen y ajusta su tamaño al tamaño de la celda
                    image = self.images[matrix[i][j]]
                    image_width, image_height = image.width(), image.height()
                    scale_factor = min(cell_size / image_width, cell_size / image_height)
                    new_width = int(image_width * scale_factor)
                    new_height = int(image_height * scale_factor)
                    # Calcula las coordenadas para centrar la imagen en la celda
                    image_x0 = x0 + (cell_size - new_width) / 2
                    image_y0 = y0 + (cell_size - new_height) / 2
                    # Dibuja la imagen ajustada y centrada
                    self.canvas.create_image(image_x0, image_y0, anchor='nw', image=image)
                else:
                    color = "white" if matrix[i][j] == 0 else "blue"
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)





# Luego, cuando creas una instancia de PacmanGUI, asegúrate de pasar el diccionario de rutas de imágenes
            
# Example usage
root = tk.Tk()
pacman_gui = PacmanGUI(root, matrix_size=len(ambiente.matriz))

for movimiento in movimientos:
    ambiente.transicion(movimiento)
    ambiente.mostrar_ambiente()
    pacman_gui.draw_matrix(ambiente.matriz)
    root.update()
    time.sleep(0.5)
    
    
    
    
    
    
    
    
    
    
# Ahora podemos verificar el estado del nuevo ambiente
# Cargar el ambiente desde el archivo
# ambiente = Ambiente()
# ambiente.cargar_desde_archivo(r'modelo\ambiente.txt')
# #print(heuristica(Nodo(ambiente)))

# # Realizar la búsqueda DFS
# camino, mensaje, nodos_expandidos, profundidad , tiempo_total = busqueda_avara(ambiente)  # Modifica esta línea

# print("Camino encontrado:", camino)
# print("Mensaje:", mensaje)
# print("Nodos expandidos:", len(nodos_expandidos))  # Agrega esta línea para mostrar los nodos expandidos
# print("Tiempo de ejecución:", tiempo_total)
# print("Profundidad:", profundidad)
# #print("Costo", costo)