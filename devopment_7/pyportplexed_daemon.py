""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
           This subprocess should return values back to a program like a thread would but over ports.
Summary: Multiplex via ports.
"""
import socket
import sys
import subprocess

""" Parse sys.argv for input arguments """
port = int(sys.argv[1])
port_1 = int(sys.argv[2])
buffer_size = int(sys.argv[3])

""" Setup socket according to input arguments """
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen()

""" Create a reusable I/O device in software that communicates over ports """
c = None
con_rcv = ''
while con_rcv != 'terminate':
    con_rcv = ''
    if c is None:

        """ Accept incoming connection """
        c, addr = s.accept()
    else:
        host_ip = s.getsockname()[0]

        """ Allow receive if incoming addr[0] (IP) == socket.getsockname()[0] """
        if host_ip == addr[0]:

            """ Decode the incoming message """
            invocation = bytes(c.recv(buffer_size)).decode('utf8')

            """ Self destruct """
            if invocation != '':
                if invocation == 'terminate':
                    break

                else:
                    """ Do some work, in this example eval() is used statically (test purposes only) CAUTION. """
                    ev = ''
                    try:
                        ev = eval(invocation)
                    except Exception as e:
                        ev = str(e)

                    """ Send the result back to the main program (note: final operation is as client) """
                    s = socket.socket()
                    host = socket.gethostname()
                    s.connect((host, port_1))

                    """ Tag result with port and send it home """
                    s.send(bytes(str(port) + ' ' + str(ev), encoding='utf-8'))
s.close()
