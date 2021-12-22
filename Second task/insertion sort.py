x=input("enter a list ")
l=[]
placeholder=0
for val in x.split():
	l.append(int(val))
def swap(x,y):
	placeholder=y
	y=x
	x=placeholder
	return x,y
for i in range(1,len(l)):
	j=i
	while (l[j]<l[j-1]) and j!=0:
		l[j],l[j-1]=swap(l[j],l[j-1])
		j-=1
print(l)