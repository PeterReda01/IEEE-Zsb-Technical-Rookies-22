def ser(alist,low,high,term):
	mid=int((high+low)/2)
	
	if(term==l[mid]):
		print(mid+1," index")
	if(term==l[mid+1]):
		print(mid+2," index")
	if(term==l[mid-1]):
		print(mid," index")
		
	elif(term>l[mid]):
		print(l)
		ser(alist,mid+1,len(l)-1,term)
		
	elif(term<l[mid]):
		ser(alist,0,mid-1,term)
		
value=int(input())
l=[1,2,3,4,5,6,7,8,9]
ser(l,0,len(l)-1,value)