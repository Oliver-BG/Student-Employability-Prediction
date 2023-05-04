import typing
from PyQt5 import QtCore, QtGui as qtw, QtCore as qtc, QtWidgets as qtw, QtGui as qtg
from PyQt5.QtWidgets import QWidget
from create_db import Record, Session, engine, create_all_table
from model import RandomForestModel

from mainWindow import Ui_MainWindow
from scoreRecord import Ui_ScoreRecord
from nameRecord import Ui_NameRecord
from resultWindow import Ui_ResultWindow

import style
import re

"""********************************* MAIN WINDOW *************************************"""

class MainWindow(qtw.QWidget):
    def __init__(self):
        """The main window for the program."""
        super().__init__()
        
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.ui_main.btn_add.clicked.connect(self.goto_add)
        self.ui_main.btn_show.clicked.connect(self.goto_record)

        self.ui_main.btn_add.setCursor(qtc.Qt.PointingHandCursor)
        self.ui_main.btn_show.setCursor(qtc.Qt.PointingHandCursor)

    def goto_add(self):
        """ Goes to the add UI """

        self.ui_name_record = NameRecord()
        widgets.addWidget(self.ui_name_record)
        widgets.setCurrentIndex(widgets.currentIndex() + 1)

    def goto_record(self):
        """ TODO """

"""********************************* NAME RECORD *************************************"""

class NameRecord(qtw.QWidget):
    def __init__(self):
        """ Opens the name record fields. """
        super().__init__()

        self.ui_name_record = Ui_NameRecord()
        self.ui_name_record.setupUi(self)

        self.ui_name_record.btn_back.clicked.connect(self.goto_main)
        self.ui_name_record.label_error.hide()

        self.last_name = None
        self.first_name = None

        self.regex_pattern = "^[a-zA-Z0-9 ]{1,}$"

        self.ui_name_record.btn_score.clicked.connect(self.goto_score_record)

    def goto_main(self):
        """ Goes back to the main window. """
        qtw.QStackedWidget.removeWidget(widgets, self)
        widgets.setCurrentIndex(widgets.currentIndex() - 1)

    def show_error(self):
        self.ui_name_record.label_error.show()

    def check_field(self, *args):
        """ Checks if the fields are not empty and is using valid characters. """
        for arg in args:
            if not arg:
                self.ui_name_record.label_error.setText("Please enter fields.")
                self.show_error() 
                return False
            
            if not re.search(self.regex_pattern, arg):
                self.ui_name_record.label_error.setText("Invalid Characters entered. Please use alphanumeric characters.")
                self.show_error() 
                return False
            
        return True

    def goto_score_record(self):
        """ Goes to the score window. """

        self.last_name = self.ui_name_record.txt_ln.text()
        self.first_name = self.ui_name_record.txt_fn.text()

        if self.check_field(self.first_name, self.last_name):
            self.ui_score_record = ScoreRecord(self.first_name, self.last_name, self)
            widgets.addWidget(self.ui_score_record)
            widgets.setCurrentIndex(widgets.currentIndex() + 1)

"""********************************* SCORE RECORD *************************************"""

class ScoreRecord(qtw.QWidget):
    def __init__(self, last_name, first_name, name_record):
        super().__init__()

        self.name_record = name_record

        self.ui_score_record = Ui_ScoreRecord()
        self.ui_score_record.setupUi(self)

        self.prediction_model = RandomForestModel()
        self.prediction = None

        self.last_name = last_name
        self.first_name = first_name

        self.ui_score_record.label_name.setText(f'Assesment for {self.first_name} {self.last_name}')
        self.ui_score_record.label_error.hide()

        # COMBO BOX

        self.combo_list = [
            self.ui_score_record.combo_general_appearance,
            self.ui_score_record.combo_manner_speaking,
            self.ui_score_record.combo_physical_condition,
            self.ui_score_record.combo_mental_alertness,
            self.ui_score_record.combo_self_confidence,
            self.ui_score_record.combo_idea_presentation,
            self.ui_score_record.combo_communication,
            self.ui_score_record.combo_student_performance
        ]

        self.info = [
            self.first_name,
            self.last_name
        ]

        self.ui_score_record.btn_predict.clicked.connect(self.predict)

        self.populate_combobox()

    def check_combobox(self):
        for combo in self.combo_list:
            if combo.SelectIndex == -1:
                self.ui_score_record.label_error.show("Please do not leave any entries empty")
                return False
        
        return True
    
    def populate_combobox(self):
        for combo in self.combo_list:
            for i in range(1,6):
                combo.addItem(str(i))
        
    def predict(self):
        for combo in self.combo_list:
            self.info.append(int(combo.currentText()))
        
        pred = self.prediction_model.make_prediction(self.info[2:])
        self.info.append(pred)

        self.goto_result()

    def goto_result(self):
        """ Shows the result. """

        self.ui_result_window = ResultWindow(self.info, self.name_record, self)
        widgets.addWidget(self.ui_result_window)
        widgets.setCurrentIndex(widgets.currentIndex() + 1)

"""********************************* RESULT WINDOW *************************************"""
        
class ResultWindow(qtw.QWidget):
    def __init__(self, info, name_record, score_record):
        super().__init__()

        self.ui_result_window = Ui_ResultWindow()
        self.ui_result_window.setupUi(self)

        self.info = info
        self.name_record = name_record
        self.score_record = score_record

        self.ui_result_window.label_name.setText(f'{self.info[0]} {self.info[1]}')

        self.result = "EMPLOYABLE" if self.info[-1] == 'Employable' else "LESS EMPLOYABLE"

        self.ui_result_window.label_pred.setText(self.result)

        print(self.info)

        self.ui_result_window.btn_save.clicked.connect(self.save_to_db)

    def save_to_db(self):
        """ Saves the record to the database. """

        session.add(Record(
            ln = self.info[0],
            fn = self.info[1],
            ga = self.info[2],
            mos = self.info[3],
            pc = self.info[4],
            ma = self.info[5],
            sc = self.info[6],
            atpi = self.info[7],
            cs = self.info[8],
            spr = self.info[9],
            pred = self.info[10],
        ))

        session.commit()

        self.go_to_main()
    
    def go_to_main(self):
        """ Goes back to the main window. """
        qtw.QStackedWidget.removeWidget(widgets, self)
        qtw.QStackedWidget.removeWidget(widgets, self.score_record)
        qtw.QStackedWidget.removeWidget(widgets, self.name_record)

        widgets.setCurrentIndex(1)


if __name__ == "__main__":

    app = qtw.QApplication([])
    app.setWindowIcon(qtg.QIcon(qtg.QPixmap("./images/window_icon.png")))

    # Main Window
    main_widget = MainWindow()
    main_widget.show()

    # Create the database
    create_all_table()

    # Cursor engine
    session = Session(bind = engine)

    widgets = qtw.QStackedWidget()
    widgets.addWidget(main_widget)
    widgets.setWindowFlags(qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowMinimizeButtonHint)
    widgets.setFixedWidth(596)
    widgets.setFixedHeight(743)
    widgets.setWindowTitle("Student Employability Predictor")
    widgets.setStyleSheet(style.widget_css)
    widgets.show()

    app.exec_()
         