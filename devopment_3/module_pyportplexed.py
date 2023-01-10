""" Written by Benjamin Jack Cullen
Intention: This module (to be) distributes workloads to n spawned subprocesses and waits for values to be
           returned.
Summary: Multiplex via ports.
"""
import socket
import subprocess


""" Setup subprocess startupinfo argument to be daemonic """
info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0


def start(port_start, end, results_port, buffer_size=1024):
    """ Starts n processes and give them a call back port number """
    ports = []
    PyPortPlexCommand = 'python ./module_pyportplexed_thread.py '
    for n in range(port_start, port_start+end):
        cmd = PyPortPlexCommand + str(n) + ' ' + str(results_port) + ' ' + str(buffer_size)
        ports.append(n)
        subprocess.Popen(cmd, startupinfo=info)
    return ports


def connect(ports):
    """ Initiate socket(s) and connect socket(s) to thread(s) (subprocess(s)) """
    socks = []
    for port in ports:
        s = socket.socket()
        host = socket.gethostname()
        s.connect((host, port))
        socks.append(s)
    return socks


def send(connections, data):
    """ Initiate socket(s) and connect socket(s) to thread(s) (subprocess(s)) """
    for connection in connections:
        connection.send(bytes(data, encoding='utf-8'))


def results(port, th, buffer_size=1024):
    """ Receive the result(s) back from the thread(s) (subprocess(s)) """
    multiplexed_results = []
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, port))
    accepted_rcv = 0
    host_ip = s.getsockname()[0]
    while accepted_rcv < th:
        s.listen()
        c, addr = s.accept()
        """ Allow receive if incoming addr[0] (IP) == socket.getsockname()[0] """
        if host_ip == addr[0]:
            multiplexed_results.append(bytes(c.recv(buffer_size)).decode('utf8'))
            accepted_rcv += 1
    s.close()
    return multiplexed_results
