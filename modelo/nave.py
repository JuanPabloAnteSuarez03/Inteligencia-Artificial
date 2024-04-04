class Nave:
    def __init__(self, fila_inicial, columna_inicial):
        self.fila = fila_inicial
        self.columna = columna_inicial
        self.estado = False
        self.contador_pasos = 0
    
    def get_posicion(self):
        return self.fila, self.columna
    
    def get_estado(self):
        return self.estado
    
    def montar_mando(self):
        self.estado = True
    
    def desmontar_mando(self):
        self.estado = False
    
    def incrementar_contador_pasos(self):
        self.contador_pasos += 1
    
    def reiniciar_contador_pasos(self):
        self.contador_pasos = 0


# Ejemplo de uso
nave = Nave(3, 3)  # Supongamos que la nave está en la fila 3, columna 3
print("Posición inicial de la nave:", nave.get_posicion())

# Mando monta la nave
nave.montar_mando()
print("¿Mando está montado en la nave?", nave.get_estado())

# Incrementar el contador de pasos de la nave
nave.incrementar_contador_pasos()
print("Contador de pasos de la nave:", nave.contador_pasos)

# Reiniciar el contador de pasos de la nave
nave.reiniciar_contador_pasos()
print("Contador de pasos de la nave reiniciado:", nave.contador_pasos)
