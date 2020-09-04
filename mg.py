import sqlite3
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
def pwd_manager_insert(name,password):
	with conn:
		if name!=' ':
			cur.execute("insert into mana values('{}','{}')".format(name,password))
			print('Succesfully inserted')
def pwd_manager_update(name,password):
	with conn:
		if name!=' ':
			cur.execute("update mana set password=:pwd where name=:name",{'pwd':password,'name':name})
		print('Succesfully updated')
def display():
	c=cur.execute('select name from mana')
	x=c.fetchall()
	d=[]
	for i in range(len(x)):
		d.append(x[i][0])
	return d
def pwd_manager_delete(name):
	with conn:
		cur.execute('delete from mana where name=:name',{'name':name})
		print('Succesfully deleted')
if __name__=='__main__':
	n=input("view  or insert or update or delete:")
	conn=sqlite3.connect('man.db')
	try:
		cur=conn.cursor()
		cur.execute('create table mana(name text,password text)')
	except:
		pass
	if n.lower()=='view':
		pwd_manager_display()
	elif n.lower()=='insert':
		name=input('Enter Name Of Website: ').strip()
		pwd=input('Enter Password: ')
		pwd_manager_insert(name,pwd)
	elif n.lower()=='update':
		print('Existing websites:')
		x=display()
		if len(x)!=0:
			print(*x)
			name=input('Enter the Name of the website for which  want to update:').strip()
			pwd=input('Enter the new password:')
			pwd_manager_update(name,pwd)
		else:
			print('No websites to update')
	elif n.lower()=='delete':
		print('Existing website:')
		x=display()
		if len(x)!=0:
			print(*x)
			name=input('Enter the name of the website to delete:').strip()
			pwd_manager_delete(name)
		else:
			print('No websites to delete')	
		
		
