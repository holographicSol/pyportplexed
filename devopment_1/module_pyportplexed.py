""" Written by Benjamin Jack Cullen
Intention: This module (to be) distributes workloads to n spawned subprocesses and waits for values to be
           returned.
Summary: Multiplex via ports.
"""
import socket
import subprocess


""" setup subprocess startupinfo argument to be daemonic """
info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0


def start(port_start, end, results_port):
    """ Starts n processes and give them a call back port number """
    commands = []
    ports = []
    for n in range(port_start, port_start+end):
        cmd = 'python ./module_pyportplexed_thread.py ' + str(n) + ' ' + str(results_port)
        ports.append(n)
        commands.append(cmd)
    [subprocess.Popen(i, startupinfo=info) for i in commands]
    return ports


def connect(ports, data):
    """ Initiate socket(s) and connect socket(s) to thread(s) (subprocess(s)) """
    socks = []
    for port in ports:
        s = socket.socket()
        host = socket.gethostname()
        s.connect((host, port))
        s.send(bytes(data, encoding='utf-8'))
        socks.append(s)
    return socks


def results(port, th):
    """ Receive the result(s) back from the thread(s) (subprocess(s)) """
    multiplexed_results = []
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, port))
    for i in range(0, th):
        s.listen()
        c, addr = s.accept()
        multiplexed_results.append(bytes(c.recv(52428800)).decode('utf8'))
    s.close()
    return multiplexed_results
