# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 268)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 341, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout__menu_inicial = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout__menu_inicial.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout__menu_inicial.setObjectName("verticalLayout__menu_inicial")
        self.frame_menu_inicial = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.frame_menu_inicial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu_inicial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu_inicial.setObjectName("frame_menu_inicial")
        self.menu_inicial_txt = QtWidgets.QLabel(self.frame_menu_inicial)
        self.menu_inicial_txt.setGeometry(QtCore.QRect(20, 12, 301, 41))
        self.menu_inicial_txt.setObjectName("menu_inicial_txt")
        self.splitter_menu_inicial = QtWidgets.QSplitter(self.frame_menu_inicial)
        self.splitter_menu_inicial.setGeometry(QtCore.QRect(100, 80, 144, 69))
        self.splitter_menu_inicial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.splitter_menu_inicial.setOrientation(QtCore.Qt.Vertical)
        self.splitter_menu_inicial.setObjectName("splitter_menu_inicial")
        self.menu_inicial_pushButton_compra = QtWidgets.QPushButton(self.splitter_menu_inicial)
        self.menu_inicial_pushButton_compra.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_inicial_pushButton_compra.setObjectName("menu_inicial_pushButton_compra")
        self.pushButton_historial = QtWidgets.QPushButton(self.splitter_menu_inicial)
        self.pushButton_historial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_historial.setObjectName("pushButton_historial")
        self.menu_inicial_pushButton_crear_cuenta = QtWidgets.QPushButton(self.splitter_menu_inicial)
        self.menu_inicial_pushButton_crear_cuenta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_inicial_pushButton_crear_cuenta.setObjectName("menu_inicial_pushButton_crear_cuenta")
        self.verticalLayout__menu_inicial.addWidget(self.frame_menu_inicial)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 21))
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
        self.menu_inicial_txt.setText(_translate("MainWindow", "Bienvenido al sistema de gestión de productos agropecuarios\n"
" Seleccione una opción"))
        self.menu_inicial_pushButton_compra.setText(_translate("MainWindow", "Comprar un producto"))
        self.pushButton_historial.setText(_translate("MainWindow", "Buscar historial"))
        self.menu_inicial_pushButton_crear_cuenta.setText(_translate("MainWindow", "Crear cuenta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
