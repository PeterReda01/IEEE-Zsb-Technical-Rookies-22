x=input()
count=0
for i in range(10):
	forward=int("".join(sorted([i for i in str(x)], reverse=True)))
	backward=int("".join(sorted([i for i in str(x)])))
	if(forward-backward==6174):
		count+=1
		print(count)
		break
	else:
		count+=1
		x=forward-backward 
		