""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
           This subprocess should return values back to a program like a thread would but over ports.
Summary: Multiplex via ports.
"""
import socket
import sys

port = int(sys.argv[1])
port_1 = int(sys.argv[2])
buffer_size = int(sys.argv[3])

s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(3)
host_ip = s.getsockname()[0]

""" Accept incoming connection """
c, addr = s.accept()

""" Allow receive if incoming addr[0] (IP) == socket.getsockname()[0] """
if host_ip == addr[0]:
    """ Decode the incoming message """
    con_rcv = bytes(c.recv(buffer_size)).decode('utf8')
    """ Do some work, in this example eval() is used statically (test purposes only) CAUTION. """
    ev = eval(con_rcv)

    """ Send the result back to the main program (note: final operation is as client) """
    s = socket.socket()
    host = socket.gethostname()
    s.connect((host, port_1))
    s.send(bytes(str(ev), encoding='utf-8'))
    s.close()
