import time
from colorama import init
from colorama import Fore, Back, Style
import os
import sys
import datetime
#init()
clear = lambda: os.system("clear")
clear()
time.sleep(1)
print(Fore.YELLOW + "-----Bitcoin-----")
time.sleep(1)
Money = 0
Bitcoin = 0
Upgrade = 0.0001
while 1 == 1:
	i = 0
	a = 0
	command = input(Fore.YELLOW +'B> '+ Fore.WHITE)
	if command == "Bitcoin":
		print(str(Bitcoin)+'B')
	elif command == "Money":
		print(str(Money)+'$')
	elif command == "Upgrade":
		if int(Money) >= 1000:
			Money = Money - 1000
			Upgrade = Upgrade + 0.0001
			print(Upgrade)
		else:
			print('No Money')

	elif command == "Bitcoin Sell":
		Money = Bitcoin * 10000
		print('Bitcoin Sell - ' + str(Money) + '$')
	elif command == "Help":
		print(' Bitcoin \n Money \n Upgrade \n Bitcoin Sell \n Upgrade Info')
	elif command == "Mining Start":
		a = (input('Bitcoin :'))
		time.sleep(2)
		while int(i) <= int(a):

			time.sleep(1)
			Bitcoin = Bitcoin + Upgrade
			i += 1
			print(Fore.GREEN +str(datetime.datetime.today())+' - '+str(i)+' - '+str(Bitcoin)+Fore.WHITE)
	elif command == "Upgrade Info":
		print(Upgrade)
		
	else:
		print(Fore.RED +'No Command'+ Fore.WHITE)



