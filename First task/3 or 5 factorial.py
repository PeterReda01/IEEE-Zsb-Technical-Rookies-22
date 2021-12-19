def summ(number):
	if (number==0):
		return 0
	elif(number%3==0) or (number%5==0):
		return number+summ(number-1)
	else:
		return summ(number-1)
x=int(input("enter number "))
print(summ(x))