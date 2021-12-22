import random as r
l=[]
for i in range(3):
	l.append(int(r.random()*9))
while(True):
	hits=0
	misses=0
	x=input("enter integer ")
	for i in l:
		z=l.index(i)
		for index,y in enumerate(x):
			if(i==int(y) and z==index):
				hits +=1
				print(z,index)
			if(i==int(y) and z!=index):
				misses +=1
				print(z,index)
	print(hits,misses)
	if(hits==3): break