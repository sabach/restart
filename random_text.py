#lista=['a', 'b', 'c','d']
#print(lista)
#for i in lista: 
#	print(i)

import random


#listb=[]
#n=int(input("insert name: "))
#for I in range (0, n):
#	ele=str(input("enter: "))
#	listb.append(ele)
#	print(listb)

listc=[]
x=int(input("enter number: "))
y=int(input("enter second number: "))
for i in range(x,y):
	listc.append(i)
	print(i)
	if i == 6:
		print("hail")
		
	else:
		continue

print("this is the list {}".format(listc))
