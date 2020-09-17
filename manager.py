import sqlite3
conn=sqlite3.connect('manager.db')
try:
	cur=conn.cursor()
	cur.execute('create table mana(website text,username text,password text)')
except:
	pass
def pwd_manager_display():
	global conn,cur
	c=cur.execute('select * from mana')
	x=c.fetchall()
	if len(x)!=0:
		for i in range(len(x)):
			print(x[i][0],end=" ")
		print()
		n=input('Enter the folder for which you want to see the username and password: ')
		for i in range(len(x)):
			if x[i][0]==n:
				print(x[i][1],x[i][2])
	else:
		print("Empty")
def pwd_manager_insert(name,username,password):
	global conn,cur
	with conn:
		if name!=' ':
			cur.execute("insert into mana values('{}','{}','{}')".format(name,username,password))
			print('Succesfully inserted')
def pwd_manager_update(name,password):
	global conn,cur
	with conn:
		if name!=' ':
			cur.execute("update mana set password=:pwd where website=:name",{'pwd':password,'name':name})
		print('Succesfully updated')
def display():
	global conn,cur
	c=cur.execute('select website from mana')
	x=c.fetchall()
	d=[]
	for i in range(len(x)):
		d.append(x[i][0])
	return d
def pwd_manager_delete(name):
	global conn,cur
	with conn:
		cur.execute('delete from mana where website=:name',{'name':name})
		print('Succesfully deleted')
def pwd_manager():
	global conn,cur
	n=input("view  or insert or update or delete:")
	if n.lower()=='view':
		pwd_manager_display()
	elif n.lower()=='insert':
		name=input('Enter Name Of Website: ').strip()
		x=display()
		if name in x:
			print("Website already Present")
			y=input('want to update? y/n')
			if y=='y':
				pwd=input('Enter new password:')
				pwd_manager_update(name,pwd)
			else:
				pass
		else:
			uname=input('Enter Username:')
			pwd=input('Enter Password: ')
			pwd_manager_insert(name,uname,pwd)
	elif n.lower()=='update':
		print('Existing websites:')
		x=display()
		if len(x)!=0:
			print(*x)
			name=input('Enter the Name of the website for which  want to update:').strip()
			pwd=input('Enter the new password:')
			#folder=Pwdmanager(name,pwd)
			pwd_manager_update(name,pwd)
		else:
			print('No websites to update')
	elif n.lower()=='delete':
		print('Existing website:')
		x=display()
		if len(x)!=0:
			print(*x)
			name=input('Enter the name of the website to delete:').strip()
			#folder=Pwdmanager(name,'')
			pwd_manager_delete(name)
		else:
			print('No websites to delete')	
if __name__=='__main__':
	pwd_manager()
		
