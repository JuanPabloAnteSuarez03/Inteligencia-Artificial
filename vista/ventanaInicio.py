from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

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

        # EJEMPLO"
        self.boton_mando_grogu = QtWidgets.QPushButton(self.frame)
        self.boton_mando_grogu.setGeometry(QtCore.QRect(420, 340, 141, 61))
        self.boton_mando_grogu.setStyleSheet("background:rgb(255, 255, 255); font-size: 11pt;")
        self.boton_mando_grogu.setObjectName("boton_mando_grogu")
        self.boton_mando_grogu.setText("Ejemplo")
        self.boton_mando_grogu.clicked.connect(self.abrir_mando_y_grogu)

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

    def abrir_mando_y_grogu(self):
        # Ejecutar "Mando y Grogu.py" usando subprocess
        subprocess.Popen(["python", "Mando y Grogu.py"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Busqueda = QtWidgets.QMainWindow()
    ui = Ui_Busqueda()
    ui.setupUi(Busqueda)
    Busqueda.show()
    sys.exit(app.exec_())
