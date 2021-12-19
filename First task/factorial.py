def summ(number):
	if (number==0):
		return 0
	else:
		return number+summ(number-1)
		
x=int(input("enter number "))
print(summ(x))