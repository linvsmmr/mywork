import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui = uic.loadUiType("morse.ui")[0]

class MyWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.button_click)
        self.show()

    def button_click(self):
        sign = self.engtext.toPlainText()
        if sign == 'a':
            sign = '.-'
        elif sign == 'b':
            sign = '-...'
        elif sign == 'c':
            sign = '-.-.'
        elif sign == 'd':
            sign = '-..'
        elif sign == 'e':
            sign = '.'
        elif sign == 'f':
            sign = '..-.'
        elif sign == 'g':
            sign = '--.'
        elif sign == 'h':
            sign = '....'
        elif sign == 'i':
            sign = '..'
        elif sign == 'j':
            sign = '.---'
        elif sign == 'k':
            sign = '-.-'
        elif sign == 'l':
            sign = '.-..'
        elif sign == 'm':
            sign = '--'
        elif sign == 'n':
            sign = '-.'
        elif sign == 'o':
            sign = '---'
        elif sign == 'p':
            sign = '.--.'
        elif sign == 'q':
            sign = '--.-'
        elif sign == 'r':
            sign = '.-.'
        elif sign == 's':
            sign = '...'
        elif sign == 't':
            sign = '-'
        elif sign == 'u':
            sign = '..-'
        elif sign == 'v':
            sign = '...-'
        elif sign == 'w':
            sign = '.--'
        elif sign == 'x':
            sign = '-..-'
        elif sign == 'y':
            sign = '-.--'
        elif sign == 'z':
            sign = '--..'
        self.fin.setText(sign)

app = QApplication(sys.argv)
window = MyWindow()
# window.show()
# app.exec_()
sys.exit(app.exec_())