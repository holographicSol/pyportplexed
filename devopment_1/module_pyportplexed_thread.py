""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
           This subprocess should return values back to a program like a thread would but over ports.
Summary: Multiplex via ports.
"""
import socket
import subprocess
import sys

port = int(sys.argv[1])
port_1 = int(sys.argv[2])

""" initiate socket and listen for a workload """
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(3)

""" accept incoming connection """
c, addr = s.accept()

""" decode the incoming message """
con_rcv = bytes(c.recv(10240)).decode('utf8')

""" do some work, in this example eval() is used statically (test purposes only) """
ev = eval(con_rcv)

""" send the result back to the main program (note: final operation is as client) """
s = socket.socket()
host = socket.gethostname()
port = port_1
s.connect((host, port_1))
s.send(bytes(str(ev), encoding='utf-8'))
s.close()
