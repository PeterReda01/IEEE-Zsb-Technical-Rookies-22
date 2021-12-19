x=int(input("enter a number"))
for i in range(2,x+1):
	for divident in range(2,x-1):
		if((i%divident)==0):
			break
		else:
			print(i)