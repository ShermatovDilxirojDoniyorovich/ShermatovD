from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QVBoxLayout,QMessageBox
from PyQt5.QtGui import QFont
import sys

app=QApplication(sys.argv)
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minioyna")
        self.setGeometry(100,100,500,500)
        self.start()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",20))
        obj.move(x,y)
    def start(self):
        ok=QPushButton("Ok",self)
        self.font(ok,50,50)

        cancel=QPushButton("Cancel",self)
        self.font(cancel,50,50)

        hbox=QHBoxLayout(self)
        hbox.addStretch()
        hbox.addWidget(ok)
        hbox.addStretch()
        hbox.addWidget(cancel)
        hbox.addStretch()

        '''vbox=QVBoxLayout(self)
        vbox.addStretch()
        vbox.addWidget(cancel)
        vbox.addWidget(ok)
        vbox.addStretch()'''

        ok.clicked.connect(self.run)
    def run(self):
        miniwindow=QMessageBox(self)
        miniwindow.setWindowTitle("Xatoliklar bilan ishlash oynasi")
        miniwindow.setText("Bu yerda dasturdagi xatoliklar chiqadi")
        miniwindow.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Reset)
        miniwindow.setDetailedText("Bu yerda xatolik bo'yicha to'liqroq ma'lumotga ega bo'lasiz")
        miniwindow.setIcon(QMessageBox.Critical)
        '''miniwindow.setIcon(QMessageBox.Question)
        miniwindow.setIcon(QMessageBox.Information)'''
        miniwindow.show()
oyna=window()
oyna.show()
app.exec_()