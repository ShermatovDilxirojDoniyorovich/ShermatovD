#  Interfeys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel,QLineEdit,QTextEdit,QPushButton
from PyQt5.QtGui import QFont
import sys

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("My first application")
window.setGeometry(200,200,400,600)
# window.setFixedWidth(500)  # Eniga kattalashtirib bo`lmaydi)
# window.setFixedHeight(500)  # Bo`yiga kattalashtirib bo`lmaydi)
# window.setFixedSize(500,500) # Umuman kattalashtirib bo`lmaydi)

# QLabel - ma`lumotlarni oynada akslantiruvchi komponenta
yozuv=QLabel("Menda yozuvlar yozildi",window)
yozuv.setFont(QFont("Times",24))
yozuv.move(100,100)

# QTextEdit va QLineEdit
line=QLineEdit(window)
line.setFont(QFont("Times",24))
line.move(100,150)

text=QTextEdit(window)
text.setFont(QFont("Times",24))
# text.setGeometry(100,250,100,100)
text.move(100,250)

# QPushButton
ok=QPushButton("Ok",window)
ok.setFont(QFont("Times",24))
ok.move(200,450)
# print(yozuv.text())
def run():
    a=line.text()
    yozuv.setText(a)
    yozuv.adjustSize()
ok.clicked.connect(run)

window.show()
app.exec_()