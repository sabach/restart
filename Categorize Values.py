#Categorize Values.py
lista=("1", "Band", "0.3", True, 0.1, 3, "Hello")
print(lista)

for item in lista:
	print("{} is data tpye of {}".format(item,type(item)))

band=str(input("type bands name: "))
listb=("Wacken", "Download", "more festivals")

for item2 in listb:
	print("{} will preform in {}".format(band, item2))

girl_name=str(input("what is the name? "))
listc=("beautiful name", "Loely name","A nice name")

for item3 in listc:
	print("{}'s name is {}".format(girl_name, item3))


listd=("pizza", "stake", "shawarma")
for item4 in listd:
	print("{},{},{} yea".format(item4[0], item4[1], item4[2], item4[3],item4[4]))
