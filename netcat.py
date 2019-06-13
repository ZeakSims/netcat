#!/bin/python
import sys
import socket

netCat   = sys.argv[1]
hostIP   = sys.argv[2]
port   = sys.argv[3]
protocol   = sys.argv[4]

if option == "-L":
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind((ip, int(port)))
   s.listen(2)

   while True:
       c, addr = s.accept()   
       print c.recv(1024)

if option == "-S":
   c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   c.connect((ip, int(port)))
   c.send("Host IP = " + ip)
   c.send("Port = " + port)
   c.send("Protocol = " + prot)

