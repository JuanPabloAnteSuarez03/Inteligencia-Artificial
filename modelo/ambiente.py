class Ambiente:
    def __init__(self):
        self.matriz = [[0] * 10 for _ in range(10)]  
        
    def inicializar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                for i, linea in enumerate(f):
                    valores = linea.strip().split()
                    for j, valor in enumerate(valores):
                        self.matriz[i][j] = int(valor)
        except FileNotFoundError:
            print("El archivo especificado no existe.")
        except Exception as e:
            print("Ocurrió un error al leer el archivo:", e)
    
    def get_casilla(self, fila, columna):
        return self.matriz[fila][columna]
    
    def mostrar_ambiente(self):
        for fila in self.matriz:
            print(' '.join(map(str, fila)))


# Ejemplo de uso
ambiente = Ambiente()
ambiente.inicializar_desde_archivo('C:/Users/jpant/OneDrive/Desktop/Universidad/Inteligencia Artificial/modelo/ambiente.txt')
ambiente.mostrar_ambiente()
