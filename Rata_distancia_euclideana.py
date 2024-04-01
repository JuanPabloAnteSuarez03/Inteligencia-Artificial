import math

def encontrar_fila_rata(matriz):
    for fila_index, fila in enumerate(matriz):
        for elemento in fila:
            if elemento == 1:
                fila_rata = fila_index
    return fila_rata

def encontrar_columna_rata(matriz):
    for fila in matriz:
        for columna_index, elemento in enumerate(fila):
            if elemento == 1:
                columna_rata = columna_index
    return columna_rata

def encontrar_fila_queso(matriz):
    for fila_index, fila in enumerate(matriz):
        for elemento in fila:
            if elemento == 3:
                fila_queso = fila_index
    return fila_queso

def encontrar_columna_queso(matriz):
    for fila in matriz:
        for columna_index, elemento in enumerate(fila):
            if elemento == 3:
                columna_queso = columna_index
    return columna_queso

def calcular_distancia(fila, columna):
    return math.sqrt((pow((encontrar_fila_queso(matriz) + 1) - (fila + 1),2) + (pow((encontrar_columna_queso(matriz) + 1) - (columna + 1),2))))

def imprimir_tablero(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

def movimientos_posibles(matriz):
    movimientos = []
    if encontrar_fila_rata(matriz) > 0 and matriz[encontrar_fila_rata(matriz) - 1][encontrar_columna_rata(matriz)] !=2: # Mover Arriba
        movimientos.append((encontrar_fila_rata(matriz) - 1, encontrar_columna_rata(matriz)))
    if encontrar_fila_rata(matriz) < len(matriz) - 1 and matriz[encontrar_fila_rata(matriz) + 1][encontrar_columna_rata(matriz)] != 2:  # Mover Abajo
        movimientos.append((encontrar_fila_rata(matriz) + 1, encontrar_columna_rata(matriz)))
    if encontrar_columna_rata(matriz) > 0 and matriz[encontrar_fila_rata(matriz)][encontrar_columna_rata(matriz) - 1] !=2:  # Mover Izquierda
        movimientos.append((encontrar_fila_rata(matriz), encontrar_columna_rata(matriz) - 1))
    if encontrar_columna_rata(matriz) < len(matriz) - 1 and matriz[encontrar_fila_rata(matriz)][encontrar_columna_rata(matriz) + 1] !=2:  # Mover Derecha
        movimientos.append((encontrar_fila_rata(matriz), encontrar_columna_rata(matriz) + 1))
    return movimientos

def mover(matriz, posicion):
    nueva_matriz = [fila[:] for fila in matriz] 
    nueva_matriz[posicion[0]][posicion[1]] = 1 
    return nueva_matriz

def encontrar_camino_mas_corto(matriz):
    movimientos_realizados = []  
    primer_mov = (encontrar_fila_rata(matriz), encontrar_columna_rata(matriz))
    movimientos_realizados.append(primer_mov)
    contador_movimientos = 0  # Inicializar contador de movimientos
    costo_total_movimiento = 0  # Inicializar el costo total de movimiento
    paso_por_5 = False  # Variable para rastrear si la rata ha pasado por un 5
    contador_pasos = 0  # Variable para contar los movimientos después de que paso_por_5 sea True
    while True:
        movimientos = movimientos_posibles(matriz)
        if not movimientos:
            print("La rata está atrapada")
            return
        
        mejor_movimiento = None
        mejor_distancia = float('inf')
        
        for fila, columna in movimientos:
            if (fila, columna) in movimientos_realizados:  
                continue
            distancia = calcular_distancia(fila, columna)
            if distancia < mejor_distancia:
                mejor_movimiento = (fila, columna)
                mejor_distancia = distancia
        matriz[primer_mov[0]][primer_mov[1]] = 0
        if mejor_movimiento is None: 
            print("La rata está atrapada")
            return
        
        if movimientos_realizados: 
            ultimo_movimiento = movimientos_realizados[-1]
            matriz[ultimo_movimiento[0]][ultimo_movimiento[1]] = 0  
        
        movimientos_realizados.append(mejor_movimiento)  
        contador_movimientos += 1  # Incrementar contador de movimientos
        
        if paso_por_5:
            costo_total_movimiento += 1  # Aumentar el costo total de movimiento en 1 si la rata ha pasado por un 5
            contador_pasos += 1  # Incrementar contador de pasos después de pasar por un 5
            if contador_pasos >= 10:  # Si ha pasado por 10 movimientos después de un 5, restablecer paso_por_5 a False
                paso_por_5 = False
                contador_pasos = 0
        else:
            costo_total_movimiento += 2  # Si no ha pasado por un 5, aumentar en 2

        if matriz[mejor_movimiento[0]][mejor_movimiento[1]] == 3:
            print("La rata ha llegado al queso.")
            print("La cantidad mínima de movimientos es:", contador_movimientos)
            print("El camino a tomar es el siguiente:", movimientos_realizados[1:])
            print("El costo total del recorrido es:", costo_total_movimiento)  # Mostrar el costo total
            movimientos_realizados.append(mejor_movimiento)
            return 
        
        if matriz[mejor_movimiento[0]][mejor_movimiento[1]] == 5:
            paso_por_5 = True
        
        matriz[mejor_movimiento[0]][mejor_movimiento[1]] = 1  
        
        print()
        imprimir_tablero(matriz)
        print()
        print(movimientos_realizados[1:])

matriz = [
    [1, 2, 0, 0, 3],
    [5, 2, 2, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0]
]

encontrar_camino_mas_corto(matriz)
