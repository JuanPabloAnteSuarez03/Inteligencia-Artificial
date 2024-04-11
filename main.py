import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from vista.ventanaInicio import Ui_Busqueda
from imagenes import fondo

def main():
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    ui = Ui_Busqueda()
    ui.setupUi(ventana)

    # Obtener la ruta absoluta del directorio actual
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta completa de la imagen
    ruta_imagen = os.path.join(ruta_actual, "vista", "fondo.jpg")

    # Verificar si la imagen existe en la ruta especificada
    if os.path.exists(ruta_imagen):
        pixmap = QPixmap(ruta_imagen)
        if not pixmap.isNull():  # Verificar si la imagen se cargó correctamente
            ui.label.setPixmap(pixmap)  # Establecer la imagen como fondo en el QLabel
        else:
            print("Error: La imagen no se cargó correctamente.")
    else:
        print("Error: La ruta de la imagen no es válida.")

    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
