x=int(input(""))
l=[]
x=input()
for val in x.split():
	l.append(int(val))
up_count=0	
down_count=0
min=0
max=0
min=l[0]
max=l[0]
for score in l:
	if(score>max):
		up_count+=1
		max=score
	elif(score<min):
		down_count+=1
		min=score
print(up_count,down_count)