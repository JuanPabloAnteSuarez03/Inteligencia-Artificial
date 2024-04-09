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
