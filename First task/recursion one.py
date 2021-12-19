def summ(alist,length):
	if (length==0):
		return l[length]
	else:
		return alist[length]+summ(alist,length-1)
#By recurtion
x=int(input("enter the size of your number list "))
l=[0]*x
z=input("enter the numbers you want in one line  ")
for enumeration,value in enumerate(z.split()):
	l[enumeration]=int(value)
	
print(summ(l,x-1))

#By for loop
summation=0
for i in l:
	summation+=i
print(summation)

#By while loop
summation=0
i=len(l)-1
while(i>-1):
	summation=summation+l[i]
	i-=1
print(summation)