import tkinter as tk

def crear_ventana():
    root = tk.Tk()
    root.title("Movimiento de Mando")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    return root, canvas

def actualizar_canvas(canvas, matriz):
    canvas.delete("all")
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            color = "white"
            if elemento == 1:
                color = "black"
            elif elemento == 2:
                color = "blue"
            elif elemento == 3:
                color = "gray"
            elif elemento == 4:
                color = "red"
            elif elemento == 5:
                color = "green"
            elif elemento == 6:
                color = "orange"  # Cambiar el color de Grogu a naranja
            canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=color)
