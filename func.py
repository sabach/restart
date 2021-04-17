def print_hello12():
	print('func that prints hello')

def ask_for_input():
	x=str(input("type hello from inside the func  "))
	print("input inside the func you have typed", x)


y=str(input("type hello from outside the func "))
def ask_for_input_outside_the_func():
	print("input outside the func you have typed", y)




z=str(input("Type user input: "))
def ask_for_input_outside_the_func_user_sdtin(z):
	
	print("input outside the func you have typed", z)



print_hello12()
ask_for_input()
ask_for_input_outside_the_func()
ask_for_input_outside_the_func_user_sdtin(z)