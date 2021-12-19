import random as r
tries=0
x=int(r.random()*10)
print("guess a number")
while(True):
	y=int(input())
	if(y==x):
		print("yup,got it ,"+str(tries)+" tries")
		break
	else:
		tries+=1
		print("wrong answer")