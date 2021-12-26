x=int(input(""))
l=[]
d={}
final=[]
l=list(input())
for type in l:
	if(type in d):
		d[type]+=1
	else:
		d[type]=1
values = d.values()
max_val = max(values)
for key,value in d.items():
	if(value==max_val):
		final.append(int(key))
print(min(final))