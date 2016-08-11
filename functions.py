import string
from config import CHANNEL

def connectToRoom(s):
	buff = ""
	loading = True
	while loading:
		buff += s.recv(1024)
		strSplt = string.split(buff, "\n")
		buff = strSplt.pop()
		
		for line in strSplt:
			print(line)
			if ("Ende der Namens liste" in line):
				loading = False

	sendToChat(s, "test")

	
def sendToChat(s, message):
	s.send("PRIVMSG #" + CHANNEL + " :" + message + "\r\n")
	print("PRIVMSG #" + CHANNEL + " :" + message)

def getUsername(line):
	subStr = line.split(":", 2)
	username = subStr[1].split("!", 1)[0]
	return username
	
def getMessage(line):
	subStr = line.split(":", 2)
	message = subStr[2]
	return message