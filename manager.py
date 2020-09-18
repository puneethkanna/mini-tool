import sqlite3
'''class Pwdmanager:
	def __init__(self,name,password):
		self.name=name
		self.password=password		'''
def pwd_manager_display(name):
	c=cur.execute('select * from mana where name=:name',{'name':name})
	x=c.fetchall()
	print(x)
	return x
	'''for i in range(len(x)):
			print(x[i][0],end=" ")
		#print()
		#n=input('Enter the folder for with we need to show the password: ')
		for i in range(len(x)):
			if x[i][0]==n:
				print(x[i][1])'''
		
	#else:
	#	print("Empty")
def pwd_manager_insert(name, pwd):
	with conn:
		c=cur.execute('select * from mana where name=:name',{'name':name})
		x=c.fetchall()
		if(name!='' and pwd!='' and pwd!=' ' and len(x) == 0):
			cur.execute("insert into mana values('{}','{}')".format(name,pwd))
			#print('Succesfully inserted')
			return True
		elif(len(x)!=0):
			return("exist")
		elif(name.isspace() or pwd.isspace()):
			return("NULL")
def pwd_manager_update(name, pwd):
	with conn:
		if name!=' ':
			cur.execute("update mana set password=:pwd where name=:name",{'pwd':pwd,'name':name})
		return True
def display():
	c=cur.execute('select name from mana')
	x=c.fetchall()
	d=[]
	for i in range(len(x)):
		d.append(x[i][0])
	return d
def pwd_manager_delete(name):
	with conn:
		c=cur.execute('select * from mana where name=:name',{'name':name})
		x=c.fetchall()
		if(len(x)!=0):
			cur.execute('delete from mana where name=:name',{'name':name})
			return True
		else:
			return False
		#print('Succesfully deleted')
#if __name__=='__main__':
#n=input("view  or insert or update or delete:")
conn=sqlite3.connect('manager.db')
try:
	cur=conn.cursor()
	cur.execute('create table mana(name text,password text)')
except:
	pass
'''if n.lower()=='view':
	pwd_manager_display()
elif n.lower()=='insert':
	name=input('Enter Name Of Website: ').strip()
	pwd=input('Enter Password: ')
	#folder=Pwdmanager(name,pwd)
	pwd_manager_insert(name, pwd)
elif n.lower()=='update':
	print('Existing websites:')
	x=display()
	if len(x)!=0:
		print(*x)
		name=input('Enter the Name of the website for which  want to update:').strip()
		pwd=input('Enter the new password:')
		#folder=Pwdmanager(name,pwd)
		pwd_manager_update(name, pwd)
	else:
		print('No websites to update')
elif n.lower()=='delete':
	print('Existing website:')
	x=display()
	if len(x)!=0:
		print(*x)
		name=input('Enter the name of the website to delete:').strip()
		folder=Pwdmanager(name,'')
		pwd_manager_delete(folder)
	else:
		print('No websites to delete')	
'''
