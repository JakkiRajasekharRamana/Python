import sys
import requests
from PySide6.QtGui     import QPixmap, QScreen
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('getAndSetImageFromURL()')
        self.label  = QLabel(self)
        self.pixmap = QPixmap()
        self.getAndSetImageFromURL(URL)
        self.resize(self.pixmap.width(),self.pixmap.height())
        screenSize = QScreen.availableGeometry(QApplication.primaryScreen())
        frmX = (screenSize.width () - self.width ())/2
        frmY = (screenSize.height() - self.height())/2
        self.move(frmX, frmY)
        self.show() 
    
    def getAndSetImageFromURL(self,imageURL):
        request = requests.get(imageURL)
        self.pixmap.loadFromData(request.content)
        self.label.setPixmap(self.pixmap)
      
class API(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Generate API')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> First Name</font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your first name')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_lname = QLabel('<font size="4"> Last Name</font>')
        self.lineEdit_lname = QLineEdit()
        self.lineEdit_lname.setPlaceholderText('Please enter your last name')
        layout.addWidget(label_lname, 1, 0)
        layout.addWidget(self.lineEdit_lname, 1, 1)
        gui = App()
        label_ID = QLabel('<font size="4"> Mail ID</font>')
        self.lineEdit_ID = QLineEdit()
        self.lineEdit_ID.setPlaceholderText('Please enter your mail ID')
        layout.addWidget(label_ID, 2, 0)
        layout.addWidget(self.lineEdit_ID, 2, 1)
#                print(label_name)
        gui = App()
        self.setLayout(layout)
        #gui = App()

if __name__ == '__main__':
    app = QApplication(sys.argv)
   # gui = App()
    form=API()
    form.show()
#    print(label_name)
    sys.exit(app.exec())
