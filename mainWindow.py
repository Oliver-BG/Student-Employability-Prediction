# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 713)
        MainWindow.setStyleSheet("background-color: #79F6C1;")
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(-10, 330, 611, 221))
        self.frame.setStyleSheet("background-color: \"#034A2C\";\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_main = QtWidgets.QLabel(self.frame)
        self.label_main.setGeometry(QtCore.QRect(0, 90, 601, 31))
        self.label_main.setStyleSheet("font-size: 24px;\n"
"background-color: \"#034A2C\";\n"
"color: \"yellow\";\n"
"")
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setObjectName("label_main")
        self.label_image = QtWidgets.QLabel(MainWindow)
        self.label_image.setGeometry(QtCore.QRect(160, 0, 311, 321))
        self.label_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("icon.png"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        self.btn_add = QtWidgets.QPushButton(MainWindow)
        self.btn_add.setGeometry(QtCore.QRect(160, 570, 271, 51))
        self.btn_add.setStyleSheet("QPushButton{\n"
"    font-size : 15px;\n"
"    background-color : \"#F87E2E\";\n"
"    color: \"white\";\n"
"    font-weight: bold;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color : \"#FFD139\";\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.btn_show = QtWidgets.QPushButton(MainWindow)
        self.btn_show.setGeometry(QtCore.QRect(160, 640, 271, 51))
        self.btn_show.setStyleSheet("QPushButton{\n"
"    font-size : 15px;\n"
"    background-color : \"#F87E2E\";\n"
"    color: \"white\";\n"
"    font-weight: bold;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color : \"#FFD139\";\n"
"}")
        self.btn_show.setObjectName("btn_show")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.label_main.setText(_translate("MainWindow", "STUDENT EMPLOYABILITY PREDICTOR"))
        self.btn_add.setText(_translate("MainWindow", "ADD RECORD"))
        self.btn_show.setText(_translate("MainWindow", "SHOW RECORDS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

