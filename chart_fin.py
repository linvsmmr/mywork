import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup
import pyautogui


form_class = uic.loadUiType("chart_fin.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)

    def btn_clicked(self):
        music_url = "https://music.bugs.co.kr/chart"
        res = requests.get(music_url)
        soup = BeautifulSoup(res.content, 'lxml')

        for i in range(len(soup.find_all('p','artist'))):
            title = soup.find_all('p','title')[i].a.string
            artist = soup.find_all('p','artist')[i].a.string
            self.tableWidget.setItem(i, 0, QTableWidgetItem(title))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(artist))
    
    def btn2_clicked(self):
        img1 = pyautogui.screenshot('scrshot.png', region=(1007,190,890,1290))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()