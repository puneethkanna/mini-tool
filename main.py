from tkinter import *  
#import password_manager as pwd_manager
import generator as ge
import manager as mg
import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox
from tkinter import Text
import random
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter import filedialog
import os
import subprocess
import ftp as ftp
import threading

LARGEFONT =("Verdana", 35)
#root = Tk()
#text = Text(root)
class miniTool(tk.Tk): 
      
    # __init__ function for class miniTool  
	def __init__(self, *args, **kwargs):
  
        # __init__ function for class Tk 
		tk.Tk.__init__(self, *args, **kwargs) 

        # creating a container 
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array 
		self.frames = {}

		# iterating through a tuple consisting 
		# of the different page layouts 
		for F in (StartPage, PasswordGenerator, PasswordManager, FileTransfer):
			frame = F(container, self)
			# initializing frame of that object from 
			# startpage, page1, PasswordManager respectively with  
			# for loop 
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")
		self.show_frame(PasswordManager)
		self.geometry("900x600")
		self.resizable(width=False, height=False)
    # to display the current frame passed as 
    # parameter 
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage 
   
class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

        # label of frame Layout 2 
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)

        # putting the grid in its place by using 
        # grid 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)
   
		button1 = ttk.Button(self, text ="Password Generator", command = lambda : controller.show_frame(PasswordGenerator)) 

        # putting the button in its place by 
        # using grid 
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)
   
        ## button to show frame 2 with text layout2 
		button2 = ttk.Button(self, text ="Password Manager", command = lambda : controller.show_frame(PasswordManager)) 
      
        # putting the button in its place by 
        # using grid 
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) 

		button3 = ttk.Button(self, text ="File Transfer", command = lambda : controller.show_frame(FileTransfer))
      
        # putting the button in its place by 
        # using grid 
		button3.grid(row = 2, column = 1, padx = 10, pady = 10) 


# second window frame page1  
class PasswordGenerator(tk.Frame): 
	def __init__(self, parent, controller):
		def pwd_generator():
			password = (ge.pwd_generator(name.get(),mail.get()))
			for p in range(len(password)):
				text_box.insert(END, password[p]+'\n')

		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Password Generator", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 
   
        # button to show frame 2 with text 
        # layout2 
		name_label = ttk.Label(self, text ="Name").grid(row = 2, column = 4)
		mail_label = ttk.Label(self, text ="Mail").grid(row = 3, column = 4)
		name = Entry(self)
		mail = Entry(self)
		name.grid(row=2, column=5)
		mail.grid(row=3, column=5)
		password_generator_ok = ttk.Button(self, text ="Generate", command = pwd_generator)
		#password_generator_ok.place(x = 50,y = 50)
		password_generator_ok.grid(row = 5, column = 5, padx = 10, pady = 10)
		button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage)) 
		#listbox = Listbox(self)
		text_box = tk.Text(self, width = 30, height = 10)
		text_box.grid(row = 6, column = 4, columnspan = 2)
        # putting the button in its place  
        # by using grid 
		button1.grid(row = 1, column = 1, padx = 20, pady = 10)
   
        # button to show frame 2 with text 
        # layout2 
		button2 = ttk.Button(self, text ="Password Manager", 
                            command = lambda : controller.show_frame(PasswordManager)) 
      
        # putting the button in its place by  
        # using grid 
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) 


# third window frame PasswordManager 
class PasswordManager(tk.Frame):  
	def __init__(self, parent, controller):
		def delete():
			pass
		def update():
			temp = (mg.pwd_manager_update(username.get(),password.get()))
			if(temp == True):
				messagebox.showinfo("Info", "Sucessfully Updated!")
		def insert():
			temp = (mg.pwd_manager_insert(username.get(),password.get()))
			if(temp == True):
				messagebox.showinfo("Info", "Sucessfully Inserted!")
			elif(temp == "exist"):
				result = messagebox.askquestion("Warning", "The username already exists, do you want to udate it??", icon='warning')
				if result == 'yes':
					update()
				else:
					pass
			elif(temp == "NULL"):
				messagebox.showinfo("Info", "No NULL Value :(")
			
		def view():
			temp = (mg.pwd_manager_display(username_view_delete.get()))
			if temp:
				messagebox.showinfo(temp[0][0], temp[0][1])
			else:
				messagebox.showinfo("Warning", "No Username Found!!")

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Password Manager", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)
		username_label = ttk.Label(self, text ="Username").grid(row = 2, column = 4)
		password_label = ttk.Label(self, text ="Password").grid(row = 3, column = 4)
		username_label_view_delete = ttk.Label(self, text ="Username").grid(row = 6, column = 4)
		username = Entry(self)
		password = Entry(self)
		username_view_delete = Entry(self)
		username.grid(row=2, column=5)
		password.grid(row=3, column=5)
		username_view_delete.grid(row=6, column=5)
		
		password_generator_ok = ttk.Button(self, text ="Insert", command= insert)
		password_generator_ok.grid(row = 5, column = 5, padx = 10, pady = 10)

		username_view_btn = ttk.Button(self, text ="View", command= view)
		#username_view_btn.grid(row = 7, column = 4, padx = 0, pady = 10)
		username_view_btn.place(x = 10, y=10)
		username_delete_btn = ttk.Button(self, text ="Delete", command= delete)
		username_delete_btn.grid(row = 7, column = 5, padx = 0, pady = 10)
        
		button1 = ttk.Button(self, text ="Password Generator", command = lambda : controller.show_frame(PasswordGenerator)) 
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text ="Startpage",  command = lambda : controller.show_frame(StartPage)) 
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

class FileTransfer(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="File Transfer", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        # button to show frame 2 with text 
        # layout2 
		def open_file():
			file = askopenfile(mode ='r', filetypes =[('All', '*.*')])

			if file is not None:
				#ttt = ftp.start_download_server(file_path=file.name, debug=1, custom_port=0, ip_addr=0, auth="puneeth:pannu123")
				#print(file.name)
				#cc = 'qr-filetransfer ' + file.name
				#p = subprocess.Popen(cc, stdout=subprocess.PIPE, shell=True)

				#(output, err) = p.communicate()
				#p_status = p.wait()
				#print("Command output : ", output)
				#print("Command exit status/return code : ", p_status)
				#stream = os.popen(cc)
				#output = stream.read()
				#print(output.strip())
				#print(ttt)
				print("")
		def open_directory():
			file = filedialog.askdirectory()
			if file is not None:
				print(file)

		select_file = ttk.Button(self, text ="OpenFile", command = lambda:open_file())
		select_file.grid(row = 5, column = 5, padx = 10, pady = 10)
		select_directory = ttk.Button(self, text ="OpenDirectory", command = lambda:open_directory())
		select_directory.grid(row = 5, column = 6, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage))
		text_box = tk.Text(self, width = 30, height = 10)

		text_box.grid(row = 6, column = 4, columnspan = 2)
        
		button1.grid(row = 1, column = 1, padx = 20, pady = 10)
   
        # button to show frame 2 with text 
        # layout2 
		button2 = ttk.Button(self, text ="Password Manager", 
                            command = lambda : controller.show_frame(PasswordManager)) 
      
        # putting the button in its place by  
        # using grid 
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) 


# Driver Code 
app = miniTool() 
app.mainloop() 
