import random

def pwd_generator(name, mail):
	#name=input('Enter your name:')
	#mail=input('Enter your mailid:')
	symbol=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
	           '*', '(', ')'] 
	#print(name, mail)			   
	n=[]
	n[:]=name
	m=[]
	m[:]=mail
	final=n+m+symbol
	password=[]
	z=''
	t1 = len(n)
	t2 = len(m)
	t1 = t1 - 3
	t2 = t2 - 3
	for i in range(5):
		z = ''
		ttt1 = random.randrange(0,t1)
		for tt1 in range(ttt1, ttt1+3):
			z = z + str(n[tt1])
		ttt2 = random.randrange(0,t2)
		for tt2 in range(ttt2, ttt2+3):
			z = z + str(m[tt2])
		for j in range(3):
			z+= str(random.choice(symbol))
		password.append(z)
		print(z)
	return(password)
		#print(z)
	#for i in password:
	#	print(i)
#password = pwd_generator()
#print(password)
