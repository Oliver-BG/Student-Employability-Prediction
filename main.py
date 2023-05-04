import typing
from PyQt5 import QtCore, QtGui as qtw, QtCore as qtc, QtWidgets as qtw, QtGui as qtg
from PyQt5.QtWidgets import QWidget
from create_db import Record, Session, engine
from model import RandomForestModel
from mainWindow import Ui_MainWindow
from scoreRecord import Ui_ScoreRecord
from nameRecord import Ui_NameRecord
import style
import re

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

        self.last_name = self.ui_name_record.txt_ln.text()
        self.first_name = self.ui_name_record.txt_fn.text()

        if self.check_field(self.first_name, self.last_name):
            self.ui_score_record = ScoreRecord(self.first_name, self.last_name)
            widgets.addWidget(self.ui_score_record)
            widgets.setCurrentIndex(widgets.currentIndex() + 2)

class ScoreRecord(qtw.QWidget):
    def __init__(self, last_name, first_name):
        super().__init__()

        self.ui_score_record = Ui_ScoreRecord()
        self.ui_score_record.setupUi(self)

        self.prediction_model = RandomForestModel()

        self.last_name = last_name
        self.first_name = first_name

        self.ui_score_record.label_name.setText(f'Assesment for {self.first_name} {self.last_name}')

if __name__ == "__main__":

    app = qtw.QApplication([])
    app.setWindowIcon(qtg.QIcon(qtg.QPixmap("./images/window_icon.png")))

    # Main Window
    main_widget = MainWindow()
    main_widget.show()

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
         