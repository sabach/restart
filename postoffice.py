user_needs=input("What do you want to buy? 1.stamps, 2. envelops, 3.make a copy?")
if user_needs == "1":
	print("Stamps")
elif user_needs=="2":
	print("envelops")
elif user_needs=="3":
	print("make copy")
	copies=input("how many copies do you need? type a number ")
	print("you need {} copies".format(copies))
else:
	print("GOod bye")