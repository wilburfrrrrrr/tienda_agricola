# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cargar productos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 361, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_cargar_cuenta = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_cargar_cuenta.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_cargar_cuenta.setObjectName("verticalLayout_cargar_cuenta")
        self.frame__cargar_cuenta = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame__cargar_cuenta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame__cargar_cuenta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame__cargar_cuenta.setObjectName("frame__cargar_cuenta")
        self.cargar_cuenta_label_cedula = QtWidgets.QLabel(self.frame__cargar_cuenta)
        self.cargar_cuenta_label_cedula.setGeometry(QtCore.QRect(80, 60, 47, 13))
        self.cargar_cuenta_label_cedula.setObjectName("cargar_cuenta_label_cedula")
        self.cargar_cuenta_label_titulo = QtWidgets.QLabel(self.frame__cargar_cuenta)
        self.cargar_cuenta_label_titulo.setGeometry(QtCore.QRect(110, 20, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cargar_cuenta_label_titulo.setFont(font)
        self.cargar_cuenta_label_titulo.setObjectName("cargar_cuenta_label_titulo")
        self.cargar_cuenta_lineEdit_cedula = QtWidgets.QLineEdit(self.frame__cargar_cuenta)
        self.cargar_cuenta_lineEdit_cedula.setGeometry(QtCore.QRect(130, 60, 111, 21))
        self.cargar_cuenta_lineEdit_cedula.setObjectName("cargar_cuenta_lineEdit_cedula")
        self.cargar_cuenta_lineEdit_nombre = QtWidgets.QLineEdit(self.frame__cargar_cuenta)
        self.cargar_cuenta_lineEdit_nombre.setGeometry(QtCore.QRect(130, 90, 111, 21))
        self.cargar_cuenta_lineEdit_nombre.setObjectName("cargar_cuenta_lineEdit_nombre")
        self.cargar_cuenta_label_nombre = QtWidgets.QLabel(self.frame__cargar_cuenta)
        self.cargar_cuenta_label_nombre.setGeometry(QtCore.QRect(80, 90, 47, 13))
        self.cargar_cuenta_label_nombre.setObjectName("cargar_cuenta_label_nombre")
        self.cargar_cuenta_pushButton_iniciar = QtWidgets.QPushButton(self.frame__cargar_cuenta)
        self.cargar_cuenta_pushButton_iniciar.setGeometry(QtCore.QRect(130, 120, 111, 23))
        self.cargar_cuenta_pushButton_iniciar.setObjectName("cargar_cuenta_pushButton_iniciar")
        self.cargar_cuenta_pushButton_volver = QtWidgets.QPushButton(self.frame__cargar_cuenta)
        self.cargar_cuenta_pushButton_volver.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.cargar_cuenta_pushButton_volver.setObjectName("cargar_cuenta_pushButton_volver")
        self.verticalLayout_cargar_cuenta.addWidget(self.frame__cargar_cuenta)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 384, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cargar_cuenta_label_cedula.setText(_translate("MainWindow", "Cédula"))
        self.cargar_cuenta_label_titulo.setText(_translate("MainWindow", "Cargar productos a"))
        self.cargar_cuenta_label_nombre.setText(_translate("MainWindow", "Nombre"))
        self.cargar_cuenta_pushButton_iniciar.setText(_translate("MainWindow", "Comprar productos"))
        self.cargar_cuenta_pushButton_volver.setText(_translate("MainWindow", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())