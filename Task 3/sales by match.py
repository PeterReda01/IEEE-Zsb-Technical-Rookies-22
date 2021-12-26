x=int(input(""))
l=[]
x=input()
for val in x.split():
	l.append(int(val))
d={}
final=[]
for type in l:
	if(type in d):
		d[type]+=1
	else:
		d[type]=1
for type,pair in d.items():
	d[type]=pair//2

print(sum(d.values()))