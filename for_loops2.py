import string
lista=[]
letters = string.ascii_lowercase
x=int(input("insert number up to 26: "))
first_letters=(letters[0:x])
end_letter=(letters[x:26])

listb=[]
user_text=str(input("enter your msg: "))
cipher=" "
char=" "
for i in user_text:
	if (ord(i)+x>122):
		#print("i am here")
		cipher=cipher+chr(ord(i)-26+x)
	else:
		cipher=cipher+chr(ord(i)+x)
	
	#listb=[i]
	#print(listb)

#x=int(input("insert number up to 26: "))
#first_letters=(letters[0:x])
#end_letter=(letters[x:26])

#print(letters)
#print(end_letter.strip()+first_letters)
print(cipher)
