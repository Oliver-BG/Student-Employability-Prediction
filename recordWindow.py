# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RecordWindow(object):
    def setupUi(self, RecordWindow):
        RecordWindow.setObjectName("RecordWindow")
        RecordWindow.resize(597, 739)
        RecordWindow.setStyleSheet("background-color: #79F6C1;;\n"
"color : white;\n"
"\n"
"QPushButton#Ok{\n"
"    background-color: #F87E2E;\n"
"    color: white;\n"
"}")
        self.container = QtWidgets.QScrollArea(RecordWindow)
        self.container.setGeometry(QtCore.QRect(0, 100, 601, 551))
        self.container.setStyleSheet("background-color: #FFE790")
        self.container.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.container.setWidgetResizable(True)
        self.container.setObjectName("container")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.container.setWidget(self.scrollAreaWidgetContents)
        self.btn_back = QtWidgets.QPushButton(RecordWindow)
        self.btn_back.setGeometry(QtCore.QRect(200, 670, 131, 41))
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
        self.label_main = QtWidgets.QLabel(RecordWindow)
        self.label_main.setGeometry(QtCore.QRect(-10, 0, 621, 51))
        self.label_main.setStyleSheet("font-size: 24px;\n"
"background-color: \"#034A2C\";\n"
"color: \"yellow\";\n"
"")
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setObjectName("label_main")

        self.retranslateUi(RecordWindow)
        QtCore.QMetaObject.connectSlotsByName(RecordWindow)

    def retranslateUi(self, RecordWindow):
        _translate = QtCore.QCoreApplication.translate
        RecordWindow.setWindowTitle(_translate("RecordWindow", "Dialog"))
        self.btn_back.setText(_translate("RecordWindow", "<< BACK"))
        self.label_main.setText(_translate("RecordWindow", "STUDENT EMPLOYABILITY PREDICTOR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RecordWindow = QtWidgets.QDialog()
    ui = Ui_RecordWindow()
    ui.setupUi(RecordWindow)
    RecordWindow.show()
    sys.exit(app.exec_())

