""" Written by Benjamin Jack Cullen
Intention: This program runs as a subprocess to do work for a program.
           This subprocess should return values back to a program like a thread would but over ports.

"""
import socket
import subprocess

""" initiate socket and listen for a workload """
s = socket.socket()
host = socket.gethostname()
port = 12348
s.bind((host, port))
s.listen(5)

while True:
    """ accept incoming connection """
    c, addr = s.accept()
    print('Connection from', addr)

    """ decode the incoming message """
    con_rcv = bytes(c.recv(10240)).decode('utf8')
    print('received:', con_rcv)

    """ do some work, in this example eval() is used statically (test purposes only) """
    print('evaluating...')
    ev = eval(con_rcv)

    """ send the result back to the main program """
    print('sending evaluated data..')
    c.send(bytes(str(ev), encoding='utf-8'))

    """ close the connection """
    if 'stop' in con_rcv:
        c.close()
