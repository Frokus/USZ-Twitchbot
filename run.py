import socket
from config import *
from functions import *


s = socket.socket()
s.connect((HOST, PORT))


s.send("PASS " + PASS + " \r\n")
s.send("NICK " + USER + " \r\n")
s.send("JOIN #" + CHANNEL + "\r\n")

connectToRoom(s)

LOOPCONTROL = True
buff = ""

while LOOPCONTROL:
	buff += s.recv(1024)
	strSplt = string.split(buff, "\n")
	buff = strSplt.pop()
	
	for line in strSplt:
		u = getUsername(line)
		m = getMessage(line)
		
		if (m[0] == '!'):
			cmd = m[1::]
			cmd = cmd.lower()
			
			if ("stopbot" in cmd):
				if (u == CHANNEL):
					LOOPCONTROL = False
			elif ("!test" in cmd):
				sendToChat(s, WHO_MESSAGE)
			
			else:
				sendToChat(s, "Unbekanter Command" + cmd)

sendToChat(s, "uszbot Offline !!!")