import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from vista.ventanaInicio import Ui_Busqueda

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_inicio = QMainWindow()
    ui = Ui_Busqueda()
    ui.setupUi(ventana_inicio)
    ventana_inicio.show()
    sys.exit(app.exec_())
