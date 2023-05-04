# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nameRecord.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NameRecord(object):
    def setupUi(self, NameRecord):
        NameRecord.setObjectName("NameRecord")
        NameRecord.resize(596, 713)
        NameRecord.setStyleSheet("background-color: #79F6C1;")
        self.btn_score = QtWidgets.QPushButton(NameRecord)
        self.btn_score.setGeometry(QtCore.QRect(350, 630, 151, 51))
        self.btn_score.setStyleSheet("QPushButton{\n"
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
        self.btn_score.setObjectName("btn_score")
        self.btn_back = QtWidgets.QPushButton(NameRecord)
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
        self.label_image = QtWidgets.QLabel(NameRecord)
        self.label_image.setGeometry(QtCore.QRect(160, 10, 311, 321))
        self.label_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("icon.png"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        self.label_main = QtWidgets.QLabel(NameRecord)
        self.label_main.setGeometry(QtCore.QRect(10, 350, 581, 31))
        self.label_main.setStyleSheet("font-size: 24px;\n"
"background-color: \"#034A2C\";\n"
"color: \"yellow\";\n"
"")
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setObjectName("label_main")
        self.txt_fn = QtWidgets.QLineEdit(NameRecord)
        self.txt_fn.setGeometry(QtCore.QRect(110, 410, 391, 31))
        self.txt_fn.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.txt_fn.setObjectName("txt_fn")
        self.label_error = QtWidgets.QLabel(NameRecord)
        self.label_error.setGeometry(QtCore.QRect(110, 570, 391, 51))
        self.label_error.setStyleSheet("font-size: 15px;\n"
"color: red;\n"
"qproperty-alignment: AlignCenter;\n"
"font-weight: bold;\n"
"\n"
"")
        self.label_error.setWordWrap(True)
        self.label_error.setObjectName("label_error")
        self.txt_ln = QtWidgets.QLineEdit(NameRecord)
        self.txt_ln.setGeometry(QtCore.QRect(110, 490, 391, 31))
        self.txt_ln.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.txt_ln.setObjectName("txt_ln")
        self.frame = QtWidgets.QFrame(NameRecord)
        self.frame.setGeometry(QtCore.QRect(-10, 340, 611, 221))
        self.frame.setStyleSheet("background-color: \"#034A2C\";\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.btn_score.raise_()
        self.btn_back.raise_()
        self.label_image.raise_()
        self.label_main.raise_()
        self.txt_fn.raise_()
        self.label_error.raise_()
        self.txt_ln.raise_()

        self.retranslateUi(NameRecord)
        QtCore.QMetaObject.connectSlotsByName(NameRecord)

    def retranslateUi(self, NameRecord):
        _translate = QtCore.QCoreApplication.translate
        NameRecord.setWindowTitle(_translate("NameRecord", "Dialog"))
        self.btn_score.setText(_translate("NameRecord", "SCORE >>"))
        self.btn_back.setText(_translate("NameRecord", "<< BACK"))
        self.label_main.setText(_translate("NameRecord", "STUDENT EMPLOYABILITY PREDICTOR"))
        self.txt_fn.setPlaceholderText(_translate("NameRecord", " F i r s t    N a m e"))
        self.label_error.setText(_translate("NameRecord", "Please Enter all fields"))
        self.txt_ln.setPlaceholderText(_translate("NameRecord", " L a s t   N a m e"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NameRecord = QtWidgets.QDialog()
    ui = Ui_NameRecord()
    ui.setupUi(NameRecord)
    NameRecord.show()
    sys.exit(app.exec_())

