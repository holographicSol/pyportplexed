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


def spawn(port_start, end, results_port, buffer_size=1024, restrained=False):
    """ Starts n process(s) each with their own port and give each of them a single call back port number """
    ports = []
    if restrained is False:
        PyPortPlexCommand = 'python ./pyportplexed_daemon.py '
    elif restrained is True:
        PyPortPlexCommand = 'python ./pyportplexed_daemon_restrained.py '
    for n in range(port_start, port_start+end):
        summon = PyPortPlexCommand + str(n) + ' ' + str(results_port) + ' ' + str(buffer_size)
        ports.append(n)
        subprocess.Popen(summon, startupinfo=info)
    return ports


def commune(ports):
    """ Initiate socket(s) and connect to the listening subprocess(s) """
    socks = []
    for port in ports:
        s = socket.socket()
        host = socket.gethostname()
        s.connect((host, port))
        socks.append(s)
    return socks


def interface(connections, data):
    """ Instruct the subprocess(s) """
    i = 0
    for connection in connections:
        connection.send(bytes(str(data[i].strip()), encoding='utf-8'))
        i += 1


def results(port, th, buffer_size=1024):
    """ Receive result(s) back from the subprocess(s) """
    multiplexed_results = []
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, port))
    accepted_rcv = 0
    l_host = s.getsockname()[0]
    while accepted_rcv < th:
        s.listen()
        c, addr = s.accept()
        """ Allow receive if incoming addr[0] == socket.getsockname()[0] """
        if l_host == addr[0]:
            resp = bytes(c.recv(buffer_size)).decode('utf8')
            idx = resp.find(' ')
            _id = resp[:idx]
            res = resp[idx+1:]
            multiplexed_results.append([_id, res])
            accepted_rcv += 1
    s.close()
    multiplexed_results = sorted(multiplexed_results, key=lambda x: x[0])
    return multiplexed_results


def destroy_daemons(connections):
    """ Destroy the daemonic process(s) """
    data = []
    for connection in connections:
        data.append('terminate')
    interface(connections, data)
