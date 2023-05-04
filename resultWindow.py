# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(596, 713)
        ResultWindow.setStyleSheet("background-color: #79F6C1;")
        self.btn_save = QtWidgets.QPushButton(ResultWindow)
        self.btn_save.setGeometry(QtCore.QRect(350, 630, 151, 51))
        self.btn_save.setStyleSheet("QPushButton{\n"
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
        self.btn_save.setObjectName("btn_save")
        self.btn_back = QtWidgets.QPushButton(ResultWindow)
        self.btn_back.setGeometry(QtCore.QRect(100, 630, 151, 51))
        self.btn_back.setStyleSheet("QPushButton{\n"
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
        self.btn_back.setObjectName("btn_back")
        self.label_image = QtWidgets.QLabel(ResultWindow)
        self.label_image.setGeometry(QtCore.QRect(160, 10, 311, 321))
        self.label_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("icon.png"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        self.label_main = QtWidgets.QLabel(ResultWindow)
        self.label_main.setGeometry(QtCore.QRect(10, 350, 581, 31))
        self.label_main.setStyleSheet("font-size: 24px;\n"
"background-color: \"#034A2C\";\n"
"color: \"yellow\";\n"
"")
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setObjectName("label_main")
        self.frame = QtWidgets.QFrame(ResultWindow)
        self.frame.setGeometry(QtCore.QRect(-10, 340, 611, 271))
        self.frame.setStyleSheet("background-color: \"#034A2C\";\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_main_2 = QtWidgets.QLabel(self.frame)
        self.label_main_2.setGeometry(QtCore.QRect(10, 60, 591, 31))
        self.label_main_2.setStyleSheet("font-size: 18px;\n"
"background-color: \"#034A2C\";\n"
"color: \"yellow\";\n"
"")
        self.label_main_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main_2.setObjectName("label_main_2")
        self.label_name = QtWidgets.QLabel(self.frame)
        self.label_name.setGeometry(QtCore.QRect(10, 110, 591, 31))
        self.label_name.setStyleSheet("font-size: 18px;\n"
"background-color: \"#034A2C\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.label_pred = QtWidgets.QLabel(self.frame)
        self.label_pred.setGeometry(QtCore.QRect(10, 150, 591, 31))
        self.label_pred.setStyleSheet("font-size: 24px;\n"
"background-color: \"#034A2C\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_pred.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pred.setObjectName("label_pred")
        self.frame.raise_()
        self.btn_save.raise_()
        self.btn_back.raise_()
        self.label_image.raise_()
        self.label_main.raise_()

        self.retranslateUi(ResultWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "Dialog"))
        self.btn_save.setText(_translate("ResultWindow", "SAVE RECORD"))
        self.btn_back.setText(_translate("ResultWindow", "<< BACK"))
        self.label_main.setText(_translate("ResultWindow", "STUDENT EMPLOYABILITY PREDICTOR"))
        self.label_main_2.setText(_translate("ResultWindow", "Assessment"))
        self.label_name.setText(_translate("ResultWindow", "<name>"))
        self.label_pred.setText(_translate("ResultWindow", "<Prediction>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultWindow = QtWidgets.QDialog()
    ui = Ui_ResultWindow()
    ui.setupUi(ResultWindow)
    ResultWindow.show()
    sys.exit(app.exec_())

