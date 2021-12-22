x =input("enter a string ")
l=[]
status=True
div=lambda x:[l.insert(0,i+1) for i in range(len(x)//2)]
div(x)
for i in l :
	if(x[i-1]!=x[-i]):
		status=False
		break
if(status==True):
	print("yes")
else:
	print("no")