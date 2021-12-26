x=int(input())
y=list(input())
count=0
sum=0
for i in y:
	if (i=='d'):
		sum-=1
	else:
		sum+=1
	if (sum==0 and i!='d'):
		count+=1
print(count)