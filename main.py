from tkinter import *  
#import password_manager as pwd_manager
import generator as ge
import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox
from tkinter import Text
import random
from tkinter import ttk

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
		self.show_frame(FileTransfer)
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
   
        button1 = ttk.Button(self, text ="Password Generator", 
        command = lambda : controller.show_frame(PasswordGenerator)) 
      
        # putting the button in its place by 
        # using grid 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
   
        ## button to show frame 2 with text layout2 
        button2 = ttk.Button(self, text ="Password Manager", 
        command = lambda : controller.show_frame(PasswordManager)) 
      
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
		
		button3 = ttk.Button(self, text ="File Transfer", 
        command = lambda : controller.show_frame(FileTransfer)) 
      
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
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Password Manager", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)
		website_label = ttk.Label(self, text ="Website").grid(row = 2, column = 4)
		password_label = ttk.Label(self, text ="Password").grid(row = 3, column = 4)
		website = Entry(self)
		password = Entry(self)
		website.grid(row=2, column=5)
		password.grid(row=3, column=5)
		password_generator_ok = ttk.Button(self, text ="Insert", )
		#password_generator_ok.place(x = 50,y = 50)
		password_generator_ok.grid(row = 5, column = 5, padx = 10, pady = 10)
        # button to show frame 2 with text 
        # layout2 
		button1 = ttk.Button(self, text ="Password Generator", command = lambda : controller.show_frame(PasswordGenerator)) 
      
        # putting the button in its place by  
        # using grid 
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text 
        # layout3 
		button2 = ttk.Button(self, text ="Startpage", 
                            command = lambda : controller.show_frame(StartPage)) 
      
        # putting the button in its place by 
        # using grid 
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

class FileTransfer(tk.Frame): 
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


# Driver Code 
app = miniTool() 
app.mainloop() 
