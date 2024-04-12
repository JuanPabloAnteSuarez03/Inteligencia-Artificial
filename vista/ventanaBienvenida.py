from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import subprocess

class Ui_Bienvenida(object):
    def setupUi(self, Bienvenida):
        Bienvenida.setObjectName("Bienvenida")
        Bienvenida.resize(700, 700)
        Bienvenida.setMinimumSize(QtCore.QSize(700, 700))
        Bienvenida.setMaximumSize(QtCore.QSize(700, 700))
        self.centralwidget = QtWidgets.QWidget(Bienvenida)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))

        # Cargar la imagen de fondo y ajustar al tamaño del frame
        self.background_image = QtGui.QPixmap("imagenes/fondo.jpg").scaled(self.frame.size())  # Ajustar tamaño
        self.background_label = QtWidgets.QLabel(self.frame)
        self.background_label.setPixmap(self.background_image)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 700, 700))

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_titulo_bienvenida = QtWidgets.QLabel(self.frame)
        self.label_titulo_bienvenida.setGeometry(QtCore.QRect(0, 20, 700, 41))
        self.label_titulo_bienvenida.setMinimumSize(QtCore.QSize(700, 41))
        self.label_titulo_bienvenida.setMaximumSize(QtCore.QSize(700, 41))
        self.label_titulo_bienvenida.setObjectName("label_titulo_bienvenida")
        self.label_miembros = QtWidgets.QLabel(self.frame)
        self.label_miembros.setGeometry(QtCore.QRect(0, 130, 700, 300))
        self.label_miembros.setMinimumSize(QtCore.QSize(700, 300))
        self.label_miembros.setMaximumSize(QtCore.QSize(700, 300))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(16)
        self.label_miembros.setFont(font)
        self.label_miembros.setObjectName("label_miembros")
        self.boton_siguiente = QtWidgets.QPushButton(self.frame)
        self.boton_siguiente.setGeometry(QtCore.QRect(300, 500, 130, 60))
        self.boton_siguiente.setMinimumSize(QtCore.QSize(130, 60))
        self.boton_siguiente.setMaximumSize(QtCore.QSize(130, 60))
        self.boton_siguiente.setStyleSheet("background:rgb(255, 255, 255); font-size: 10pt; font-family:Bell MT;")
        self.boton_siguiente.setObjectName("boton_siguiente")
        self.boton_siguiente.clicked.connect(self.abrir_siguiente)
        Bienvenida.setCentralWidget(self.centralwidget)

        self.retranslateUi(Bienvenida)
        QtCore.QMetaObject.connectSlotsByName(Bienvenida)

    def retranslateUi(self, Bienvenida):
        _translate = QtCore.QCoreApplication.translate
        Bienvenida.setWindowTitle(_translate("Bienvenida", "Busqueda"))
        self.label_titulo_bienvenida.setText(_translate("Bienvenida", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-family:Bell MT; color:#ffffff;\">ALGORITMOS DE BÚSQUEDA</span></p></body></html>"))
        self.label_miembros.setText(_translate("Bienvenida", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Juan Pablo Ante - 2140132</span></p><p align=\"center\"><span style=\" color:#ffffff;\">Nicolas Garcés - 2180066</span></p><p align=\"center\"><span style=\" color:#ffffff;\">Alejandro Guerrero - 2179652</span></p><p align=\"center\"><span style=\" color:#ffffff;\">Alejandro Zamorano - 1941088</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.boton_siguiente.setText(_translate("Bienvenida", "SIGUIENTE"))

    def abrir_siguiente(self):
        # Ejecutar "Mando y Grogu.py" usando subprocess
        subprocess.Popen(["python", "vista/ventanaInicio.py"])
         # Ocultar la ventana actual
        app = QApplication.instance()
        app.activeWindow().hide()
"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bienvenida = QtWidgets.QMainWindow()
    ui = Ui_Bienvenida()
    ui.setupUi(Bienvenida)
    Bienvenida.show()
    sys.exit(app.exec_())"""
