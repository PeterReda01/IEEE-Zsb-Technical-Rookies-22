x=input("enter a list ")
l=[]
y=[]
distance=[]
for val in x.split():
	l.append(int(val))

for num1 in range(len(l)):
	for num2 in range(num1+1,len(l)):
		if(l[num1]==l[num2]):
			y.append(tuple((num1,num2)))
for tup in y:
	distance.append(tup[1]-tup[0])
print(min(distance))