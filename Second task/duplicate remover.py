x=input("enter a list ")
l=x.split()
d={}
for i in l:
	d[int(i)]=i
print(list(d.keys()))