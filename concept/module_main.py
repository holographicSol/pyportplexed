""" Written by Benjamin Jack Cullen
Intention: This module distributes workloads to n spawned subprocesses and waits for values to be
           returned.

"""
import socket

""" initiate socket and connect socket to thread (subprocess) """
s = socket.socket()
host = socket.gethostname()
port = 12348
s.connect((host, port))
print('Connected to', host)

while True:
    """ 1. temporary input in place of function args in ultimately a module. """
    z = input("evaluate: ")

    """ 2. send data to be evaluated to the thread (subprocess) """
    s.send(bytes(z, encoding='utf-8'))

    """ 3. receive the result back from the thread (subprocess) """
    result = bytes(s.recv(10240)).decode('utf8')
    print('received evaluation:', result)

    """ close the connection """
    if 'stop' in z:
        s.close()
