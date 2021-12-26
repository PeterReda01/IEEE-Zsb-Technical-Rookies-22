total=int(input())
destination=int(input())
count=0
check=[]
l=[]
if(destination==1):
	print(0)
else:
	count+=1
	for i in range(total//2):
		l.clear()
		l.append(2*(i+1))
		l.append(2*(i+1)+1)
		if destination in l:
			break
		else:
			count+=1
print(count)