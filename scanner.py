#!/bin/python3

import sys
import socket
from datetime import datetime

#Define the Target 

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Traslate HostName to IPv4
else:
	print("INVALID AMOUNT OF ARGUMENTS ")
	print("SYNTAX : python3 scanner.py <ip>")

#BANNER 
print("-" *80)
print("Scanning Target:"+target)
print("Time Started : " +str(datetime.now()))

try:
	for port in range(50,90): #anyrange btw 65535 | Taking 50-90 coz of DNS :) 
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result ==0:
			print(f"The port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting Program T_T")
	sys.exit()

except socket.gaierror:
	print("\nHostName could not resolved T_T")
	sys.exit()

except socket.error:
	print("\nCould not connect to the server T_T")
	sys.exit()
	
