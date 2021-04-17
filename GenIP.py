#first get from user pub or privet
#and print a public ip or privte ip
import random

def pri_ip10():
	privte_octect1 = str(random.randint(10,10))
	privte_octect2 = str(random.randint(0,255))
	privte_octect3 = str(random.randint(0,255))
	privte_octect4 = str(random.randint(0,255))
	return privte_octect1+"."+privte_octect2+"."+privte_octect3+"."+privte_octect4

print(pri_ip10())



def pri_ip192():
	privte_octect1 = str(192.168)
	privte_octect2 = str(random.randint(0,255))
	privte_octect3 = str(random.randint(0,255))
	return privte_octect1+"."+privte_octect2+"."+privte_octect3

print(pri_ip192())