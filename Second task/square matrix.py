import copy
x=int(input(""))
reverse=[]
total=[]
one=[]
sum=0
for i in range(x):
	x=input()
	for val in x.split():
		one.append(int(val))
	total.append(copy.deepcopy(one))
	one.clear()
for i in range(len(total)):
	sum+=total[i][i]
reverse=list(copy.deepcopy(reversed(total)))
for i in reversed(range(len(reverse))):
	sum-=reverse[i][i]
print(sum)