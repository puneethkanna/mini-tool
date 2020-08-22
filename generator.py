import random
name=input('Enter your name:')
mail=input('Enter your mailid:')
symbol=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')'] 
n=[]
n[:0]=name
m=[]
m[:0]=mail
final=n+m+symbol
password=[]
for i in range(5):
	z=''
	for j in range(12):
		z+=random.choice(final)
	password.append(z)
for i in password:
	print(i)
