import requests
from os import system, name


if name == 'nt': 
	_ = system('cls') 
else: 
	_ = system('clear') 

def all857() : 
	f = open("sites.txt")
	sites = f.read().splitlines()
	i = 1
	for url in sites:
		http = False
		https = False

		try:
			r = requests.get("http://"+ url)
			rContent = str(r.content, 'utf-8')
			check1 = "http://www.airtel.in/dot/" not in rContent
			check2 = "Department of Telecommunications" not in rContent
			if r.ok and (check1 and check2) :
				http = True	
		except:
			http = False

		try:	
			rContent = str(r.content, 'utf-8')
			check1 = "http://www.airtel.in/dot/" not in rContent
			check2 = "Department of Telecommunications" not in rContent
			if r.ok and (check1 and check2):
				https = True
		except:
			https = False 

		print (str(i) + "\tHTTP: " + str(http) + "\tHTTPS: " + str(https) + "\t" + url)
		i+=1

def top100() :
	print("Checking TOP 100 Sites")
	print("----------------------")
	f = open("top100.txt")
	sites = f.read().splitlines()
	i = 1
	for url in sites:
		http = False
		https = False

		try:
			r = requests.get("http://" + url)
			rContent = str(r.content, 'utf-8')
			check1 = "http://www.airtel.in/dot/" not in rContent
			check2 = "Department of Telecommunications" not in rContent
			if r.ok and (check1 and check2):
				http = True
		except:
			http = False

		try:
			rContent = str(r.content, 'utf-8')
			check1 = "http://www.airtel.in/dot/" not in rContent
			check2 = "Department of Telecommunications" not in rContent
			if r.ok and (check1 and check2):
				https = True
		except:
			https = False

		print(str(i) + "\tHTTP: " + str(http) +
		      "\tHTTPS: " + str(https) + "\t" + url)
		i += 1

if __name__ == "__main__":
	print("Chalo Charkha Chalae | ✊✊✊💦 | 🖕🖕🖕💧")
	print("-----------------------------------------------")
	print("Choice\tSearch Mode")
	print("------\t-----------")
	print("1\t All 857 Sites Banned Sites")
	print("2\t Top 100 Porn Sites")
	choice = int(input("\n\nEnter Choice: "))
	print("\n")
	if choice == 1 :
		all857()
	elif choice == 2 : 
		top100()
	else :
		all857()
	
	print("\n\n Happy Quarantine 😉")
