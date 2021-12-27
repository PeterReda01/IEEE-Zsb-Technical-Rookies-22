# this code has some bugs
x=input()
arr1=input()
arr2=input()
l=[]
factors=set()
fact2=set()
arr1=list(map(int,list(arr1.split())))

for element in arr2.split():
	l.append(int(element))
for value in l:
	for whole_number in range(2, value + 1):
		if value % whole_number == 0:
			factors.add(whole_number)
	if (len(fact2)==0):
		fact2=factors.copy()
		factors.clear()
		continue
	else:
		fact2=fact2.intersection(factors)
print(fact2)
for i in fact2:
	for val in range(len(arr1)):
		if i%arr1[val] !=0:
			break
		if (arr1[val]%i==0) and (val==len(arr1)-1):
			print(i)