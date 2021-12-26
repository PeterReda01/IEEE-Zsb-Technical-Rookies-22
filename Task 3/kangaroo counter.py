l=list(input())
l=list(map(int,l))
intersection=0
if(l[1]==l[3]):
	print("no")
else:
	intersection=  (l[2]-l[0])/(l[1]-l[3])
	if(intersection<l[0])and (intersection<l[2]):
		print("no")
	else:
		print("yes")