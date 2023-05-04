from PyQt5 import QtGui as qtw, QtCore as qtc, QtWidgets as qtw
from create_db import Record, Session, engine
from model import model



if __name__ == "__main__":
    session = Session(bind = engine)
         
