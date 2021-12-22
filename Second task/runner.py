x=int(input("enter no. of iterations "))
s=set()
y=input()
for val in y.split():
	s.add(int(val))
l=list(s)
l.sort(reverse=True)
print(l[1])