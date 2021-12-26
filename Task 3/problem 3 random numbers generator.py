import string
import random
total=[]
l=random.randint(1,8) #l stands for letters
nums=random.randint(1,9-l)
spec=10-nums-l #spec stands for special characters
total.append(list(random.choice(string.ascii_letters) for i in range(l) ))
total.append(list(str(random.randint(0,10)) for i in range(nums)))
total.append(list(random.choice(["@","$","#","%","&"]) for i in range(spec)))
total=total[0]+total[1]+total[2]
random.shuffle(total)
print( '\033[1m'+   ''.join(total))
# i used this code ('\033[1m') to just make the password in bold format so that it's more readable.