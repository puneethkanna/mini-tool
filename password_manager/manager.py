import sqlite3
from pwdmanager import Pwdmanager
def pwd_manager_display():
	c=cur.execute('select * from mana')
	x=c.fetchall()
	
	if len(x)!=0:
		for i in range(len(x)):
			print(x[i][0],end=" ")
		print()
		n=input('Enter the folder for with we need to show the password: ')
		for i in range(len(x)):
			if x[i][0]==n:
				print(x[i][1])
	else:
		print("Empty")
def pwd_manager_insert(folder):
	with conn:
		if folder.name!=' ':
			cur.execute("insert into mana values ('{}','{}')".format(folder.name,folder.password))
			print('Succesfully inserted')
if __name__=='__main__':
	x=input("View  or insert ")
	conn=sqlite3.connect('manager.db')
	try:
		cur=conn.cursor()
		cur.execute('create table mana(name text,password text)')
	except:
		pass
	if x=='view':
		pwd_manager_display()
	else:
		name=input('Enter Name Of Website: ')
		pwd=input('Enter Password: ')
		folder=Pwdmanager(name,pwd)
		pwd_manager_insert(folder)
	

