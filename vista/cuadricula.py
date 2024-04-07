import tkinter as tk

def crear_ventana():
    root = tk.Tk()
    root.title("Movimiento de Mando")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    canvas.image_references = []  # Crear una lista vacía para mantener las referencias de las imágenes
    return root, canvas

def actualizar_canvas(canvas, matriz):
    canvas.delete("all")
    img_width = 50
    img_height = 50
    
    # Lista de las rutas de las imágenes correspondientes a cada elemento
    image_paths = {
        1: "imagenes/negro.png",
        2: "imagenes/mandalorian.png",
        3: "imagenes/nave.png",
        4: "imagenes/darthVader.png",
        5: "imagenes/grogu.png",
        6: "imagenes/mandalorian_y_grogu.png"
    }
    
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            img_path = image_paths.get(elemento)
            if img_path:
                img = tk.PhotoImage(file=img_path)
                # Calcular la posición de inicio de la imagen para que esté centrada en la celda de la cuadrícula
                start_x = j * img_width + (img_width - img.width()) // 2
                start_y = i * img_height + (img_height - img.height()) // 2
                canvas.create_image(start_x, start_y, anchor=tk.NW, image=img)
                canvas.image_references.append(img)  # Mantén una referencia a la imagen
