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

        if matriz[mejor_movimiento[0]][mejor_movimiento[1]] == 3:
            print("La rata ha llegado al queso.")
            print("La cantidad minima de movimientos es", len(movimientos_realizados[1:]))
            print("El camino a tomar es el siguiente:", movimientos_realizados[1:])
            movimientos_realizados.append(mejor_movimiento)
            return 
        
        matriz[mejor_movimiento[0]][mejor_movimiento[1]] = 1  
        
        print()
        imprimir_tablero(matriz)
        print()
        print(movimientos_realizados[1:])

matriz = [
    [0, 0, 0, 0, 3],
    [0, 0, 2, 2, 0],
    [0, 1, 2, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0]
]

encontrar_camino_mas_corto(matriz)