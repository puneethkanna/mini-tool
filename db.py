import sqlite3
from PyQt5.QtWidgets import QMessageBox
conn=sqlite3.connect('man.db')
try:
	cur=conn.cursor()
	cur.execute('create table mana(website text,username text,password text)')
except:
	pass
def insert(website,username,password):
	global conn,cur
	msg=QMessageBox()
	with conn:
		if website!=' ':
			cur.execute("insert into mana values('{}','{}','{}')".format(website,username,password))
			msg.setWindowTitle("MiniTool")
			msg.setText("Data Succesfully inserted")
			x=msg.exec_()
def display():
	global conn,cur
	c=cur.execute('select website from mana')
	x=c.fetchall()
	d=[]
	for i in range(len(x)):
		d.append(x[i][0])
	return d
def viewfolder():
	global conn,cur
	x=display()
	msg=QMessageBox()
	msg.setWindowTitle("MiniTool")
	s=""
	#print(x)
	for i in range(len(x)):
		s+=x[i]+"\n"
	msg.setText(s)
	y=msg.exec_()
def delete(website):
	global conn,cur
	msg=QMessageBox()
	with conn:
		cur.execute('delete from mana where website=:name',{'name':website})
		msg.setWindowTitle("Minitool")
		msg.setText("Data Succesfully deleted")
		x=msg.exec_()
		
def view(website):
	x=display()
	msg=QMessageBox()
	msg.setWindowTitle("Minitool")
	if website in x:
		c=cur.execute('select username,password from mana where website=:name',{'name':website})
		y=c.fetchall()
		msg.setText("Username   : "+y[0][0]+"\n"+"Password   : "+y[0][1])
		z=msg.exec_()
	else:
		msg.setText("Invalid Website")
		z=msg.exec_()
	
	
