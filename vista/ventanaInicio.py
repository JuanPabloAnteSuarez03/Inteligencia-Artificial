from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modelo'))

import tkinter as tk
from tkinter import messagebox
from busqueda import *
from cuadricula import *
import subprocess
from functools import partial

class Ui_Busqueda(object):
    def setupUi(self, Busqueda):
        Busqueda.setObjectName("Busqueda")
        Busqueda.resize(700, 700)
        Busqueda.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)  # Bloquear botón de maximizar
        self.centralwidget = QtWidgets.QWidget(Busqueda)
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
        self.label_titulo = QtWidgets.QLabel(self.frame)
        self.label_titulo.setGeometry(QtCore.QRect(6, 1, 691, 41))
        self.label_titulo.setWordWrap(True)
        self.label_titulo.setObjectName("label_titulo")
        self.label_no_informada = QtWidgets.QLabel(self.frame)
        self.label_no_informada.setGeometry(QtCore.QRect(60, 120, 231, 31))
        self.label_no_informada.setObjectName("label_no_informada")
        self.boton_profundidad = QtWidgets.QPushButton(self.frame)
        self.boton_profundidad.setGeometry(QtCore.QRect(100, 180, 141, 61))
        self.boton_profundidad.setStyleSheet("background:rgb(255, 255, 255); font-size: 11pt;")
        self.boton_profundidad.setObjectName("boton_profundidad")
        self.boton_amplitud = QtWidgets.QPushButton(self.frame)
        self.boton_amplitud.setGeometry(QtCore.QRect(100, 260, 141, 61))
        self.boton_amplitud.setStyleSheet("background:rgb(255, 255, 255); font-size: 11pt;")
        self.boton_amplitud.setObjectName("boton_amplitud")
        self.boton_costo = QtWidgets.QPushButton(self.frame)
        self.boton_costo.setGeometry(QtCore.QRect(100, 340, 141, 61))
        self.boton_costo.setStyleSheet("background:rgb(255, 255, 255); font-size: 11pt;")
        self.boton_costo.setObjectName("boton_costo")
        self.boton_avara = QtWidgets.QPushButton(self.frame)
        self.boton_avara.setGeometry(QtCore.QRect(420, 260, 141, 61))
        self.boton_avara.setStyleSheet("background:rgb(255, 255, 255); font-size: 11pt;")
        self.boton_avara.setObjectName("boton_avara")
        self.label_informada = QtWidgets.QLabel(self.frame)
        self.label_informada.setGeometry(QtCore.QRect(375, 120, 231, 31))
        self.label_informada.setObjectName("label_informada")
        self.boton_a = QtWidgets.QPushButton(self.frame)
        self.boton_a.setGeometry(QtCore.QRect(420, 180, 141, 61))
        self.boton_a.setStyleSheet("background:rgb(255, 255, 255); font-size: 11pt;")
        self.boton_a.setObjectName("boton_a")

        Busqueda.setCentralWidget(self.centralwidget)

        self.retranslateUi(Busqueda)
        QtCore.QMetaObject.connectSlotsByName(Busqueda)

    def retranslateUi(self, Busqueda):
        _translate = QtCore.QCoreApplication.translate
        Busqueda.setWindowTitle(_translate("Busqueda", "Busqueda"))
        self.label_titulo.setText(_translate("Busqueda", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:white;\">ALGORITMOS DE BUSQUEDA</span></p></body></html>"))
        self.label_no_informada.setText(_translate("Busqueda", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:white;\">NO INFORMADA</span></p></body></html>"))
        self.boton_profundidad.setText(_translate("Busqueda", "Profundidad"))
        self.boton_amplitud.setText(_translate("Busqueda", "Amplitud"))
        self.boton_costo.setText(_translate("Busqueda", "Costo"))
        self.boton_avara.setText(_translate("Busqueda", "AVARA"))
        self.label_informada.setText(_translate("Busqueda", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:white;\">INFORMADA</span></p></body></html>"))
        self.boton_a.setText(_translate("Busqueda", "A*"))

    def abrir_cuadricula(self):
        # Ejecutar "cuadricula.py" usando subprocess
        subprocess.Popen(["python", "vista/cuadricula.py"])

class VentanaInicio(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ventana de Inicio")
        self.ui = Ui_Busqueda()
        self.ui.setupUi(self)

        self.ui.boton_profundidad.clicked.connect(self.ejecutar_busqueda_profundidad)
        self.ui.boton_amplitud.clicked.connect(self.ejecutar_busqueda_amplitud)
        self.ui.boton_costo.clicked.connect(self.ejecutar_busqueda_costo_uniforme)
        self.ui.boton_avara.clicked.connect(self.ejecutar_busqueda_avara)
        self.ui.boton_a.clicked.connect(self.ejecutar_busqueda_a)

    def ejecutar_busqueda_profundidad(self):
        movimientos, mensaje, nodos_expandidos, profundidad, tiempo = busqueda_profundidad(ambiente)
        ejecutar_busqueda_y_mostrar_cuadricula(ambiente, movimientos)
        self.mostrar_resultados(mensaje, nodos_expandidos, profundidad, tiempo)

    def ejecutar_busqueda_amplitud(self):
        movimientos, mensaje, nodos_expandidos, profundidad, tiempo = busqueda_amplitud(ambiente)
        ejecutar_busqueda_y_mostrar_cuadricula(ambiente, movimientos)
        self.mostrar_resultados(mensaje, nodos_expandidos, profundidad, tiempo)

    def ejecutar_busqueda_costo_uniforme(self):
        movimientos, mensaje, nodos_expandidos, profundidad, tiempo, costo = busqueda_costo_uniforme(ambiente)
        ejecutar_busqueda_y_mostrar_cuadricula(ambiente, movimientos)
        self.mostrar_resultados(mensaje, nodos_expandidos, profundidad, tiempo, costo)

    def ejecutar_busqueda_avara(self):
        movimientos, mensaje, nodos_expandidos, profundidad, tiempo, costo = busqueda_avara(ambiente)
        ejecutar_busqueda_y_mostrar_cuadricula(ambiente, movimientos)
        self.mostrar_resultados(mensaje, nodos_expandidos, profundidad, tiempo, costo)
    
    def ejecutar_busqueda_a(self):
        movimientos, mensaje, nodos_expandidos, profundidad, tiempo, costo = a_estrella(ambiente)
        ejecutar_busqueda_y_mostrar_cuadricula(ambiente, movimientos)
        self.mostrar_resultados(mensaje, nodos_expandidos, profundidad, tiempo, costo)

    def mostrar_resultados(self, mensaje, nodos_expandidos, profundidad, tiempo, costo=None):
        resultados = f"Mensaje: {mensaje}\nProfundidad: {profundidad}\nTiempo de ejecución: {tiempo}"
        if costo is not None:
            resultados += f"\nCosto: {costo}"
        QtWidgets.QMessageBox.information(self, "Resultados", resultados) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_inicio = VentanaInicio()
    ventana_inicio.show()
    sys.exit(app.exec_())