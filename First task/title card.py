y=input("enter a title ")
z=y.split()
num=[]
maxx=lambda z:[num.append(len(i)) for i in z]
maxx(z)
m=max (num)
print("**"+"*" *(m+4))
for i in z:
	print("**",i+" "*(m-len(i)),"**")
print("**"+"*" *(m+4))