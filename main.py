import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from vista.ventanaInicio import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_inicio = VentanaInicio()
    ventana_inicio.show()
    sys.exit(app.exec_())