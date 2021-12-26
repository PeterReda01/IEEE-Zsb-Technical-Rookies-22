import copy
x=int(input(""))
total=[]
one=[]
for i in range(x):
	x=input()
	for val in x.split():
		one.append(int(val))
	total.append(copy.deepcopy(one))
	one.clear()
s=list(list(zip(*total))[1])
s.sort(reverse=True)
if(sum(list(zip(*total))[0])<(s[0]+s[1])):
	print("yes")
else:
	print("no")