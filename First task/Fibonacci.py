last_number=1
first_number=0
sum=1
num=int(input("enter a number"))
print(0)
for i in range(num-1):
	print(sum)
	sum=first_number+last_number
	first_number=last_number
	last_number=sum