#i=1
#while i < 6:
#	print(i)
#	i+=1


import random
x=int(input("insert number: "))
i=0
n=random.randint(0,3)
#print(n)
	
while n == x:
	print(i)
	i+=1

print ("{} is the number you typed".format(x))
print ("{} is the number chosen".format(n))