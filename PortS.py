# Python 2.7
# Port Scanner
# Kali Linux
# Tel localho3t
# Email mr.localho3t@yahoo.com

#---------------------

import requests as re
from socket import *
import sys as ar
from os import system
from time import sleep
import datetime

#---------------------

def banner():
	print """
 _ _ _                              _ _ _
| | | | [!] Exploit TM         [!] | | | | 
| | | | [!] LocalHo3t          [!] | | | |
\_/_\_/ [!] Port Scaner V 1.3  [!] \_/_\_/ 
\ | | /	[!] 8 SEP 2020         [!] \ | | /
 \| |/ 	[!] 00:51 TH           [!]  \| |/ 
  \_/   [!] Next Update : NONE [!]   \_/  
"""

#---------------------
def help():
	print """
-SS : python portS.py -SS
-AK : python portS.py -AK --time 40
-TA : python portS.py -TA [Target IP] --time 40


-i  : [ip] {Str}
-p  : [port] {Int}
Example : python portS.py -i 192.168.1.1 -p 80
"""

#---------------------
def main():
	try:
		if ar.argv[1] == '--help':
			help()
			
			ar.exit()
		if (ar.argv[1] == '-SS'):
			for q in range(1,65400):
				s = socket(AF_INET,SOCK_STREAM)
				re = s.connect_ex(('127.0.0.1',q))
				if(re == 0):
					print q
			ar.exit()
		if (ar.argv[1] == '-AK') & (ar.argv[2] == '--time'):#0050
			while(1):
				
				for i in range(1,65400):
					s = socket(AF_INET,SOCK_STREAM)
					re = s.connect_ex(('127.0.0.1',i))
					if(re == 0):
						print i
				sleep(int(ar.argv[3]))
				print "---{}---".format(datetime.datetime.now().strftime('[%H:%M:%S]'))
				
			ar.exit()
		if (ar.argv[1] == '-TA') & (ar.argv[3] == '--time'):#0050
			url = ar.argv[2]
			while(1):
				
				for i in range(1,65400):
					s = socket(AF_INET,SOCK_STREAM)
					re = s.connect_ex((url,i))
					if(re == 0):
						print i
				sleep(int(ar.argv[4]))
				print "---{}---".format(datetime.datetime.now().strftime('[%H:%M:%S]'))
				
			ar.exit()

		if (ar.argv[1] == '-i') & (ar.argv[3] == '-p'):
				url= ar.argv[2]
				port = int(ar.argv[4])
				s = socket(AF_INET,SOCK_STREAM)
				re = s.connect_ex((url,port))
				if(re == 0):
					print "OPEN"
				else:
					print "CLOSE"
		
			
	except Exception as e:
		print e
		print "python portS.py --help"
#---------------------
if __name__ == "__main__":
	try:
		system('clear')
		banner()
		main()
	except KeyboardInterrupt as e:
		print "\nGood By :)"


#---------------------
