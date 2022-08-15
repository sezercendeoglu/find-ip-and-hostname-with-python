import socket as soc #importing socket library.then we write soc instead of socket with as function.

myHost=soc.gethostname()
#Generate variable which name is myHost. It can find Host Name.
print("Your hostname: "+myHost)
myIP=soc.gethostbyname(myHost)
#Generate variable which name is myIP. It can find IP Number.
print("Your IP: "+myIP)
