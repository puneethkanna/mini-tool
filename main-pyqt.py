import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import generator as ge
import manager as mg

#from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
#from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.title = "App"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500
		self.InitUI()

	def InitUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)

		buttonWindow1 = QPushButton('Password Generator', self)
		buttonWindow1.move(100, 100)
		buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
		buttonWindow1.adjustSize()
		#self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", self)
		#self.lineEdit1.setGeometry(250, 100, 400, 30)

		buttonWindow2 = QPushButton('Password Manager', self)
		buttonWindow2.move(100, 200)
		buttonWindow2.clicked.connect(self.buttonWindow2_onClick)
		buttonWindow2.adjustSize()
		#self.lineEdit2 = QLineEdit("Type here what you want to transfer for [Window2].", self)
		#self.lineEdit2.setGeometry(250, 200, 400, 30)

		buttonWindow3 = QPushButton('File Transfer', self)
		buttonWindow3.move(100, 300)
		buttonWindow3.clicked.connect(self.buttonWindow3_onClick)
		buttonWindow3.adjustSize()
		#self.lineEdit3 = QLineEdit("Type here what you want to transfer for [Window2].", self)
		#self.lineEdit3.setGeometry(250, 200, 400, 30)

		self.show()

	@pyqtSlot()
	def buttonWindow1_onClick(self):
		self.statusBar().showMessage("Switched to window 1")
		self.cams = PasswordGenerator(self) 
		self.cams.show()
		self.close()

	@pyqtSlot()
	def buttonWindow2_onClick(self):
		self.statusBar().showMessage("Switched to window 2")
		self.cams = PasswordManager(self) 
		self.cams.show()
		self.close()

	@pyqtSlot()
	def buttonWindow3_onClick(self):
		self.statusBar().showMessage("Switched to window 2")
		self.cams = FileTransfer(self) 
		self.cams.show()
		self.close()

class PasswordGenerator(QDialog):
	def __init__(self, value, parent=None):
		super().__init__(parent)
		self.setGeometry(100, 100, 680, 550) 
		self.setWindowTitle('Password Generator')
		widget = QWidget()
		#listWidget = QListWidget()
		self.formGroupBox = QGroupBox("Password Generator")
		self.listWidget = QListWidget()
		self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)

		dlgLayout = QVBoxLayout()
		self.formLayout = QFormLayout()
        
		self.name = QLineEdit()
		self.mail = QLineEdit()
		self.createForm()   
                
		self.window_layout = QVBoxLayout(widget)
		self.window_layout.addWidget(self.listWidget)
		widget.setLayout(self.window_layout)
		dlgLayout.addWidget(self.formGroupBox)

		dlgLayout.addLayout(self.formLayout)
		dlgLayout.addLayout(self.window_layout)
		#dlgLayout.addLayout(self.formGroupBox)
		#dlgLayout.addLayout()
        
        

		self.generate_btn = QPushButton(self)
		self.generate_btn.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.generate_btn.setText('Generate')
		self.generate_btn.clicked.connect(self.generate)

		self.pushButton = QPushButton(self)
		self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.pushButton.setText('Home')
		self.pushButton.clicked.connect(self.goMainWindow)
        
		dlgLayout.addWidget(self.generate_btn)
		dlgLayout.addWidget(self.pushButton)

		self.setLayout(dlgLayout)

	def createForm(self): 
		layout = QFormLayout() 
		layout.addRow(QLabel("Name"), self.name)
		layout.addRow(QLabel("Mail"), self.mail)
		self.formGroupBox.setLayout(layout)

	@pyqtSlot()
	def generate(self):
		password = (ge.pwd_generator(self.name.text(),self.mail.text()))
		self.listWidget = QListWidget()
		self.formLayout.addRow(self.listWidget)
    #listWidget = QListWidget()
		for p in range(len(password)):
			QListWidgetItem(password[p] , self.listWidget)
        #self.window_layout.setLayout(self.listWidget)
        
	def goMainWindow(self):
		self.cams = Window()
		self.cams.show()
		self.close() 


class PasswordManager(QDialog):
	def __init__(self, value, parent=None):
		super().__init__(parent)
		self.setGeometry(100, 100, 530, 500) 
		self.setWindowTitle('Password Manager')
		widget = QWidget()
		#listWidget = QListWidget()
		self.AddUpdateBox = QGroupBox("Add Password")
		self.DeletePasswordBox = QGroupBox("Delete Password")
		self.listWidget = QListWidget()
		self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)

		dlgLayout = QVBoxLayout()
		self.formLayout = QFormLayout()
		#self.formLayout1 = QFormLayout()
        
		self.add_update_username = QLineEdit()
		self.add_update_password = QLineEdit()
		self.delete_username = QLineEdit()
		self.AddUpdateForm()
                
		self.window_layout = QVBoxLayout(widget)
		self.window_layout.addWidget(self.listWidget)
		widget.setLayout(self.window_layout)  

		self.add_update_btn = QPushButton(self)
		self.add_update_btn.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.add_update_btn.setText('Add')
		self.add_update_btn.clicked.connect(self.add_update)

		self.delete_btn = QPushButton(self)
		self.delete_btn.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.delete_btn.setText('Delete')
		self.delete_btn.clicked.connect(self.delete)
        
		self.DeleteForm()

		self.pushButton = QPushButton(self)
		self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.pushButton.setText('Home')
		self.pushButton.clicked.connect(self.goMainWindow)

		dlgLayout.addWidget(self.AddUpdateBox)
		dlgLayout.addWidget(self.add_update_btn)
		dlgLayout.addWidget(self.DeletePasswordBox)
		dlgLayout.addWidget(self.delete_btn)
		dlgLayout.addLayout(self.formLayout)
		dlgLayout.addLayout(self.window_layout)    

		dlgLayout.addWidget(self.pushButton)

		self.setLayout(dlgLayout)

	def AddUpdateForm(self): 
		layout = QFormLayout() 
		layout.addRow(QLabel("Username"), self.add_update_username)
		layout.addRow(QLabel("Password"), self.add_update_password)
		self.AddUpdateBox.setLayout(layout)
	def DeleteForm(self):
		layout = QFormLayout() 
		layout.addRow(QLabel("Username"), self.delete_username)
		self.DeletePasswordBox.setLayout(layout)


	@pyqtSlot()
	def add_update(self):
		temp = (mg.pwd_manager_insert(self.add_update_username.text(),self.add_update_username.text()))
		if(temp == True):
			QMessageBox.about(self, "Info", "New password added sucessfully!")
		elif(temp == "exist"):
			result = QMessageBox.question(self, 'Warning', "The username already exists, do you want to udate it??", QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
			if(result == QMessageBox.Yes):
				self.update()
			else:
				pass
		elif(temp == "NULL"):
			QMessageBox.about(self, "Info", "No NULL Value :(")

	@pyqtSlot()
	def delete(self):
		temp = (mg.pwd_manager_delete(self.delete_username.text()))
		if(temp == True):
			QMessageBox.about(self, "Info", "Password deleted sucessfully!")
		elif(temp == False):
			QMessageBox.critical(self, "Warning", "No username found!!")
		
	
	@pyqtSlot()
	def update(self):
		temp = (mg.pwd_manager_update(self.add_update_username.text(),self.add_update_password.text()))
		if(temp == True):
			QMessageBox.about(self, "Info", "Password updated sucessfully!")

	def goMainWindow(self):
		self.cams = Window()
		self.cams.show()
		self.close()

class FileTransfer(QDialog):
	def __init__(self, value, parent=None):
		super().__init__(parent)
		self.setGeometry(100, 100, 680, 550) 
		self.setWindowTitle('Password Generator')
		widget = QWidget()
		#listWidget = QListWidget()
		self.formGroupBox = QGroupBox("Password Generator")
		self.listWidget = QListWidget()
		self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)

		dlgLayout = QVBoxLayout()
		self.formLayout = QFormLayout()
        
		self.name = QLineEdit()
		self.mail = QLineEdit()
		self.createForm()   
                
		self.window_layout = QVBoxLayout(widget)
		self.window_layout.addWidget(self.listWidget)
		widget.setLayout(self.window_layout)
		dlgLayout.addWidget(self.formGroupBox)

		dlgLayout.addLayout(self.formLayout)
		dlgLayout.addLayout(self.window_layout)
		#dlgLayout.addLayout(self.formGroupBox)
		#dlgLayout.addLayout()
        
        

		self.generate_btn = QPushButton(self)
		self.generate_btn.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.generate_btn.setText('Generate')
		self.generate_btn.clicked.connect(self.generate)

		self.pushButton = QPushButton(self)
		self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.pushButton.setText('Home')
		self.pushButton.clicked.connect(self.goMainWindow)
        
		dlgLayout.addWidget(self.generate_btn)
		dlgLayout.addWidget(self.pushButton)

		self.setLayout(dlgLayout)

	def createForm(self): 
		layout = QFormLayout() 
		layout.addRow(QLabel("Name"), self.name)
		layout.addRow(QLabel("Mail"), self.mail)
		self.formGroupBox.setLayout(layout)

	@pyqtSlot()
	def generate(self):
		password = (ge.pwd_generator(self.name.text(),self.mail.text()))
		self.listWidget = QListWidget()
		self.formLayout.addRow(self.listWidget)
    #listWidget = QListWidget()
		for p in range(len(password)):
			QListWidgetItem(password[p] , self.listWidget)
        #self.window_layout.setLayout(self.listWidget)
        
	def goMainWindow(self):
		self.cams = Window()
		self.cams.show()
		self.close() 


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Window()
    sys.exit(app.exec_())