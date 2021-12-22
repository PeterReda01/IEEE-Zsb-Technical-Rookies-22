import copy
x=int(input("nter the number of iterables "))
one=[]
total=[]
names=[]
s=set()
for i in range(x):
	y=input()
	z=int(input())
	one.append(y)
	one.append(z)
	total.append(copy.deepcopy(one))
	one.clear()
for student in total:
	s.add(student[1])
l=list(s)
l.sort()
for i in total:
	if (i[1]==l[1]):
		names.append(i[0])
names.sort()
for name in names:
	print(name)