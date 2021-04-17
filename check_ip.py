#create func that gets an ip addr
#and returns false if its 
#and true if its public
#lista = ["192.168", "10.0", "172.16", "169.254" , "127.0"]

def CheckIP():


	user_ip=input(str("type the ip: "))
	temp_ip=user_ip.split(".")
	first_oct=str(temp_ip[0])
	second_oct=str(temp_ip[1])

	ip_to_compare=(str(first_oct+"."+second_oct))
	print(ip_to_compare)

	if ip_to_compare == str(192.168):
		print ("private")
	elif ip_to_compare == str(10.0) or str(10.10):
		print ("private")
	elif ip_to_compare == str(172.16):
		print ("private")
	elif ip_to_compare == str(127.0):
		print ("private")
	elif ip_to_compare == str(169.254):
		print ("private")
	else:
		print("public")

CheckIP()