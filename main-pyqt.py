import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import generator as ge
import manager as mg
import ftp
import subprocess
import threading
import time
import qrcode
from io import BytesIO
from PyQt5 import QtCore, QtGui
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

		buttonWindow3 = QPushButton('Send Files', self)
		buttonWindow3.move(100, 300)
		buttonWindow3.clicked.connect(self.buttonWindow3_onClick)
		buttonWindow3.adjustSize()
		
		buttonWindow4 = QPushButton('Recieve Files', self)
		buttonWindow4.move(100, 400)
		buttonWindow4.clicked.connect(self.buttonWindow4_onClick)
		buttonWindow4.adjustSize()

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
		#self.statusBar().showMessage("Switched to window 2")
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		#options |= QFileDialog.DontUseCustomDirectoryIcons
		global fileName
		#dialog = QFileDialog()
		#dialog.setOptions(options)
		#QFileDialog.getExistingDirectory
		#result = QMessageBox.question(self, 'Choose', "Select File or Folder?", QMessageBox.File | QMessageBox.Folder, QMessageBox.Folder)
		#if(result == QMessageBox.Folder):
		#	fileName = QFileDialog.getExistingDirectory(self,"Choose")
		#else:
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			print("ttttttt"+fileName)
			#tt = "qr-filetransfer " + fileName
			#ftp_test.demo(fileName)
			#self.fileName = fileName
			threading.Thread(target=self.mini_download, daemon=True).start()
			time.sleep(3)
			print(ftp.mini_download_url)
			print(ftp.mini_download_ssid)
			#FileTransfer().show()
			self.cams = FileTransferDownload() 
			self.cams.show()
		#self.close()

	def mini_download(self):
			ftp.start_download_server(fileName, debug=1, custom_port=0, ip_addr=0)

	@pyqtSlot()
	def buttonWindow4_onClick(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		global fileName
		#result = QMessageBox.question(self, 'Choose', "Select File or Folder?", QMessageBox.File | QMessageBox.Folder, QMessageBox.Folder)
		#if(result == QMessageBox.Folder):
		fileName = QFileDialog.getExistingDirectory(self,"Choose")
		#else:
		#fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			print("ttttttt"+fileName)
			threading.Thread(target=self.mini_upload, daemon=True).start()
			time.sleep(3)
			print(ftp.mini_upload_url)
			print(ftp.mini_upload_ssid)
			#FileTransfer().show()
			self.cams = FileTransferUpload() 
			self.cams.show()
		#self.close()

	def mini_upload(self):
			ftp.start_upload_server(fileName, debug=1, custom_port=0, ip_addr=0)
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

		self.AddUpdateBox = QGroupBox("Add Password")
		self.DeletePasswordBox = QGroupBox("Delete Password")
		self.listWidget = QListWidget()
		self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)

		dlgLayout = QVBoxLayout()
		self.formLayout = QFormLayout()
        
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

class FileTransferDownload(QWidget):
	def __init__(self):
		super().__init__()
		#self.setGeometry(100, 100, 680, 550) 
		self.setWindowTitle('Files Send')
		#self.horizontalGroupBox = QGroupBox(ftp.mini_message)
		Vlayout = QVBoxLayout()
		Hlayout = QHBoxLayout()
		label = QLabel()
		ssid_label = QLabel()
		url_label = QLabel()
		qr_image = qrcode.make(ftp.mini_download_url, image_factory = Image).pixmap()
		#Vlayout.addWidget(QLabel("Make sure your other device is connected to ").setAlignment(QtCore.Qt.AlignCenter))
		ssid_label.setText(ftp.mini_download_ssid)
		ssid_label.setStyleSheet("color: blue;font-size:60px;")
		ssid_label.setAlignment(QtCore.Qt.AlignCenter)
		Hlayout.addWidget(ssid_label)
		#M_Label = label.setText(ftp.mini_message)
		#I_Label = label.setPixmap(qr_image)
		label.setPixmap(QPixmap(qr_image))
		label.setAlignment(QtCore.Qt.AlignCenter)

		Vlayout.addLayout(Hlayout)
		Vlayout.addWidget(label)

		urlLink="<a href="+ftp.mini_download_url +">" +ftp.mini_download_url + "</a>"
		url_label.setText(urlLink)

		Vlayout.addStretch(1)
		Vlayout.addWidget(url_label)

		url_label.setAlignment(QtCore.Qt.AlignCenter)
		url_label.setOpenExternalLinks(True)
		url_label.setStyleSheet("font-size:22px;")

		self.resize(qr_image.width()+20,qr_image.height()+40)
		self.setMaximumSize(qr_image.width()+30,qr_image.height()+50)
		self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
		self.setLayout(Vlayout)

	def print_qr_code(address):
		qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
		qr.add_data(address)
		qr.make()

	def goMainWindow(self):
		self.cams = Window()
		self.cams.show()
		self.close() 

class FileTransferUpload(QWidget):
	def __init__(self):
		super().__init__()
		#self.setGeometry(100, 100, 680, 550) 
		self.setWindowTitle('Files Recieve')
		#self.horizontalGroupBox = QGroupBox(ftp.mini_message)
		Vlayout = QVBoxLayout()
		Hlayout = QHBoxLayout()
		label = QLabel()
		ssid_label = QLabel()
		url_label = QLabel()
		qr_image = qrcode.make(ftp.mini_upload_url, image_factory = Image).pixmap()
		#Vlayout.addWidget(QLabel("Make sure your other device is connected to ").setAlignment(QtCore.Qt.AlignCenter))
		ssid_label.setText(ftp.mini_upload_ssid)
		ssid_label.setStyleSheet("color: blue;font-size:60px;")
		ssid_label.setAlignment(QtCore.Qt.AlignCenter)
		Hlayout.addWidget(ssid_label)
		#M_Label = label.setText(ftp.mini_message)
		#I_Label = label.setPixmap(qr_image)
		label.setPixmap(QPixmap(qr_image))
		label.setAlignment(QtCore.Qt.AlignCenter)
		Vlayout.addLayout(Hlayout)
		Vlayout.addWidget(label)

		urlLink="<a href="+ftp.mini_upload_url +">" +ftp.mini_upload_url + "</a>"
		url_label.setText(urlLink)

		Vlayout.addStretch(1)
		Vlayout.addWidget(url_label)

		url_label.setAlignment(QtCore.Qt.AlignCenter)
		url_label.setOpenExternalLinks(True)
		url_label.setStyleSheet("font-size:22px;")
		self.resize(qr_image.width()+20,qr_image.height()+40)
		self.setMaximumSize(qr_image.width()+30,qr_image.height()+50)
		self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
		self.setLayout(Vlayout)

	def goMainWindow(self):
		self.cams = Window()
		self.cams.show()
		self.close() 

class Image(qrcode.image.base.BaseImage): 
  
    # constructor 
	def __init__(self, border, width, box_size): 
  
        # assigning border 
		self.border = border 
  
        # assigning  width 
		self.width = width 
  
        # assigning box size 
		self.box_size = box_size 
  
        # creating size 
		size = (width + border * 2) * box_size 
  
        # image 
		self._image = QImage(size, size, QImage.Format_RGB16) 
  
        # initial image as white 
		self._image.fill(Qt.white) 
  
  
    # pixmap method 
	def pixmap(self): 
  
        # returns image 
		return QPixmap.fromImage(self._image) 
  
    # drawrect method for drawing rectangle 
	def drawrect(self, row, col): 
  
        # creating painter object 
		painter = QPainter(self._image) 
  
        # drawing rectangle 
		painter.fillRect( 
            (col + self.border) * self.box_size, 
            (row + self.border) * self.box_size, 
            self.box_size, self.box_size, 
            QtCore.Qt.black) 

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Window()
    sys.exit(app.exec_())