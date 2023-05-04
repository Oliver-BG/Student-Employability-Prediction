# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scoreRecord.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScoreRecord(object):
    def setupUi(self, ScoreRecord):
        ScoreRecord.setObjectName("ScoreRecord")
        ScoreRecord.resize(590, 712)
        self.frame_2 = QtWidgets.QFrame(ScoreRecord)
        self.frame_2.setGeometry(QtCore.QRect(-10, 250, 611, 381))
        self.frame_2.setStyleSheet("background-color: \"#026728\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_main = QtWidgets.QLabel(self.frame_2)
        self.label_main.setGeometry(QtCore.QRect(20, 10, 581, 31))
        self.label_main.setStyleSheet("font-size: 24px;\n"
"background-color: \"#026728\";\n"
"color: \"yellow\";\n"
"")
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setObjectName("label_main")
        self.combo_general_appearance = QtWidgets.QComboBox(self.frame_2)
        self.combo_general_appearance.setGeometry(QtCore.QRect(200, 90, 69, 22))
        self.combo_general_appearance.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.combo_general_appearance.setObjectName("combo_general_appearance")
        self.combo_manner_speaking = QtWidgets.QComboBox(self.frame_2)
        self.combo_manner_speaking.setGeometry(QtCore.QRect(200, 150, 69, 22))
        self.combo_manner_speaking.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.combo_manner_speaking.setObjectName("combo_manner_speaking")
        self.label_name = QtWidgets.QLabel(self.frame_2)
        self.label_name.setGeometry(QtCore.QRect(10, 50, 591, 21))
        self.label_name.setStyleSheet("font-size: 18px;\n"
"background-color: \"#026728\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.combo_physical_condition = QtWidgets.QComboBox(self.frame_2)
        self.combo_physical_condition.setGeometry(QtCore.QRect(200, 210, 69, 22))
        self.combo_physical_condition.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.combo_physical_condition.setObjectName("combo_physical_condition")
        self.combo_mental_alertness = QtWidgets.QComboBox(self.frame_2)
        self.combo_mental_alertness.setGeometry(QtCore.QRect(200, 270, 69, 22))
        self.combo_mental_alertness.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.combo_mental_alertness.setObjectName("combo_mental_alertness")
        self.combo_idea_presentation = QtWidgets.QComboBox(self.frame_2)
        self.combo_idea_presentation.setGeometry(QtCore.QRect(500, 150, 69, 22))
        self.combo_idea_presentation.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.combo_idea_presentation.setObjectName("combo_idea_presentation")
        self.combo_self_confidence = QtWidgets.QComboBox(self.frame_2)
        self.combo_self_confidence.setGeometry(QtCore.QRect(500, 90, 69, 22))
        self.combo_self_confidence.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.combo_self_confidence.setObjectName("combo_self_confidence")
        self.combo_student_performance = QtWidgets.QComboBox(self.frame_2)
        self.combo_student_performance.setGeometry(QtCore.QRect(500, 270, 69, 22))
        self.combo_student_performance.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.combo_student_performance.setObjectName("combo_student_performance")
        self.combo_communication = QtWidgets.QComboBox(self.frame_2)
        self.combo_communication.setGeometry(QtCore.QRect(500, 210, 69, 22))
        self.combo_communication.setStyleSheet("border-radius : 5px;\n"
"font-family: \"sans-serif\";\n"
"height : 34px;\n"
"font-weight: 1;\n"
"background-color : \"#FFFFFF\";\n"
"border : 1px solid;\n"
"font-size: 18px;")
        self.combo_communication.setObjectName("combo_communication")
        self.label_ga = QtWidgets.QLabel(self.frame_2)
        self.label_ga.setGeometry(QtCore.QRect(20, 90, 181, 21))
        self.label_ga.setStyleSheet("font-size: 18px;\n"
"background-color: \"#02220E\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_ga.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_ga.setObjectName("label_ga")
        self.label_mos = QtWidgets.QLabel(self.frame_2)
        self.label_mos.setGeometry(QtCore.QRect(20, 150, 181, 21))
        self.label_mos.setStyleSheet("font-size: 18px;\n"
"background-color: \"#02220E\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_mos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_mos.setObjectName("label_mos")
        self.label_pc = QtWidgets.QLabel(self.frame_2)
        self.label_pc.setGeometry(QtCore.QRect(20, 210, 171, 21))
        self.label_pc.setStyleSheet("font-size: 18px;\n"
"background-color: \"#02220E\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_pc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_pc.setObjectName("label_pc")
        self.label_ma = QtWidgets.QLabel(self.frame_2)
        self.label_ma.setGeometry(QtCore.QRect(20, 270, 171, 21))
        self.label_ma.setStyleSheet("font-size: 18px;\n"
"background-color: \"#02220E\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_ma.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_ma.setObjectName("label_ma")
        self.label_sc = QtWidgets.QLabel(self.frame_2)
        self.label_sc.setGeometry(QtCore.QRect(320, 90, 181, 21))
        self.label_sc.setStyleSheet("font-size: 18px;\n"
"background-color: \"#034A2C\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_sc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_sc.setObjectName("label_sc")
        self.label_ip = QtWidgets.QLabel(self.frame_2)
        self.label_ip.setGeometry(QtCore.QRect(320, 150, 181, 21))
        self.label_ip.setStyleSheet("font-size: 18px;\n"
"background-color: \"#034A2C\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_ip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_ip.setObjectName("label_ip")
        self.label_c = QtWidgets.QLabel(self.frame_2)
        self.label_c.setGeometry(QtCore.QRect(320, 210, 181, 21))
        self.label_c.setStyleSheet("font-size: 18px;\n"
"background-color: \"#034A2C\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_c.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_c.setObjectName("label_c")
        self.label_sp = QtWidgets.QLabel(self.frame_2)
        self.label_sp.setGeometry(QtCore.QRect(320, 270, 181, 21))
        self.label_sp.setStyleSheet("font-size: 18px;\n"
"background-color: \"#034A2C\";\n"
"color: \"#FAB244\";\n"
"")
        self.label_sp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_sp.setObjectName("label_sp")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(10, 80, 291, 301))
        self.frame.setStyleSheet("background-color: \"#02220E\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(300, 80, 301, 301))
        self.frame_3.setStyleSheet("background-color: \"#034A2C\";")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.raise_()
        self.frame.raise_()
        self.label_main.raise_()
        self.combo_general_appearance.raise_()
        self.combo_manner_speaking.raise_()
        self.label_name.raise_()
        self.combo_physical_condition.raise_()
        self.combo_mental_alertness.raise_()
        self.combo_idea_presentation.raise_()
        self.combo_self_confidence.raise_()
        self.combo_student_performance.raise_()
        self.combo_communication.raise_()
        self.label_ga.raise_()
        self.label_mos.raise_()
        self.label_pc.raise_()
        self.label_ma.raise_()
        self.label_sc.raise_()
        self.label_ip.raise_()
        self.label_c.raise_()
        self.label_sp.raise_()
        self.label_image_2 = QtWidgets.QLabel(ScoreRecord)
        self.label_image_2.setGeometry(QtCore.QRect(180, 10, 231, 231))
        self.label_image_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_image_2.setText("")
        self.label_image_2.setPixmap(QtGui.QPixmap("icon.png"))
        self.label_image_2.setScaledContents(True)
        self.label_image_2.setObjectName("label_image_2")
        self.btn_back = QtWidgets.QPushButton(ScoreRecord)
        self.btn_back.setGeometry(QtCore.QRect(220, 650, 151, 51))
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
        self.btn_back_2 = QtWidgets.QPushButton(ScoreRecord)
        self.btn_back_2.setGeometry(QtCore.QRect(20, 650, 151, 51))
        self.btn_back_2.setStyleSheet("QPushButton{\n"
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
        self.btn_back_2.setObjectName("btn_back_2")
        self.btn_back_3 = QtWidgets.QPushButton(ScoreRecord)
        self.btn_back_3.setGeometry(QtCore.QRect(420, 650, 151, 51))
        self.btn_back_3.setStyleSheet("QPushButton{\n"
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
        self.btn_back_3.setObjectName("btn_back_3")

        self.retranslateUi(ScoreRecord)
        QtCore.QMetaObject.connectSlotsByName(ScoreRecord)

    def retranslateUi(self, ScoreRecord):
        _translate = QtCore.QCoreApplication.translate
        ScoreRecord.setWindowTitle(_translate("ScoreRecord", "Dialog"))
        self.label_main.setText(_translate("ScoreRecord", "STUDENT EMPLOYABILITY PREDICTOR"))
        self.label_name.setText(_translate("ScoreRecord", "<text name here>"))
        self.label_ga.setText(_translate("ScoreRecord", "General Appeareance"))
        self.label_mos.setText(_translate("ScoreRecord", "Manner of Speaking"))
        self.label_pc.setText(_translate("ScoreRecord", "Physical Condition"))
        self.label_ma.setText(_translate("ScoreRecord", "Mental Alertness"))
        self.label_sc.setText(_translate("ScoreRecord", "Self Confidence"))
        self.label_ip.setText(_translate("ScoreRecord", "Idea Presentation"))
        self.label_c.setText(_translate("ScoreRecord", "Communication"))
        self.label_sp.setText(_translate("ScoreRecord", "Student Performance "))
        self.btn_back.setText(_translate("ScoreRecord", "<< BACK TO MAIN"))
        self.btn_back_2.setText(_translate("ScoreRecord", "<< BACK "))
        self.btn_back_3.setText(_translate("ScoreRecord", "PREDICT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScoreRecord = QtWidgets.QDialog()
    ui = Ui_ScoreRecord()
    ui.setupUi(ScoreRecord)
    ScoreRecord.show()
    sys.exit(app.exec_())

