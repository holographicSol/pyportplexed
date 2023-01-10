""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import time
import pyportplexed

start_port = 55555
results_port = 12345


def simple_example_0():
    """ Send something for PyPortPlexed to compute and then destroy the daemons """

    n_threads = 4

    """ 1. Start daemonic processes with args """
    ports = pyportplexed.start(start_port, n_threads, results_port, buffer_size=1024)

    """ 2. Connect to daemonic processes """
    connections = pyportplexed.connect(ports)

    data = ['10**1', '10**2', '10**3', '10**4']

    print('Starting Program X: Using PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.send(connections, data=data)

    """ Wait for the results to come in from PyPortPlexed """
    results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(results))

    """ Destroy the daemonic process(s) when done """
    pyportplexed.destroy_daemons(connections)

    for result in results:
        print('result _id:', result[0], ' result:', result[1])


def simple_example_1():
    """ Send something for PyPortPlexed to compute and then destroy the daemons """

    n_threads = 8

    """ 1. Start daemonic processes with args """
    ports = pyportplexed.start(start_port, n_threads, results_port, buffer_size=1024)

    """ 2. Connect to daemonic processes """
    connections = pyportplexed.connect(ports)

    data = ['1024**100000', '1024**100000', '1024**100000', '1024**100000',
            '1024**100000', '1024**100000', '1024**100000', '1024**100000']

    print('Starting Program X: Using PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.send(connections, data=data)

    """ Wait for the results to come in from PyPortPlexed """
    results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(results))

    """ Destroy the daemonic process(s) when done """
    pyportplexed.destroy_daemons(connections)


def simple_example_2():
    """ Send something for PyPortPlexed to compute then send
    PyPortPlexed some more data to compute and then destroy the daemons
    """

    n_threads = 8

    """ 1. Start daemonic processes with args """
    ports = pyportplexed.start(start_port, n_threads, results_port, buffer_size=1024)

    """ 2. Connect to daemonic processes """
    connections = pyportplexed.connect(ports)

    data = ['1024**100000', '1024**100000', '1024**100000', '1024**100000',
            '1024**100000', '1024**100000', '1024**100000', '1024**100000']

    """ Operation 1. """
    print('Starting Program X: Using PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.send(connections, data=data)
    results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(results))

    """ Operation 2. """
    print('Sending another workload for PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.send(connections, data=data)
    second_results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(second_results))

    """ Destroy the daemonic process(s) when done """
    pyportplexed.destroy_daemons(connections)


def simple_example_3():
    """ Send PyPortPlexed different data to compute
    """

    n_threads = 2

    """ 1. Start daemonic processes with args """
    ports = pyportplexed.start(start_port, n_threads, results_port, buffer_size=1024)

    """ 2. Connect to daemonic processes """
    connections = pyportplexed.connect(ports)

    data = ['subprocess.getoutput("powershell ping 8.8.8.8")',
            'subprocess.getoutput("powershell ping 9.9.9.9")']

    """ Operation """
    print('Starting Program X: Using PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.send(connections, data=data)
    results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(results))

    """ Destroy the daemonic process(s) when done """
    pyportplexed.destroy_daemons(connections)


# uncomment to test
simple_example_0()
# simple_example_1()
# simple_example_2()
# simple_example_3()
"""
(8 operations: 1024**100000)
my pyportplexed (python -OO program_x.py):
    (8 operations: 1024**100000) 2.0330955000026734 seconds

single thread (python -OO time_equivalent_eval(1024^10000).py):
    (8 operations: 1024**100000) 16.447089799999958 seconds


(8 operations: 1024**500000)
my pyportplexed (python -OO program_x.py):
    (8 operations: 1024**500000) 58.40562380000483 seconds (<1 minute)

single thread (python -OO time_equivalent_eval(1024^50000).py):
    (8 operations: 1024**500000) 361.5826317000028 seconds (6+ minutes)


(Ping Example)
my pyportplexed (python -OO program_x.py):
    (Ping 2 addresses in simultaniously) 6.025762999983272 seconds

single thread (python -OO time_equivalent_eval(ping_two_addresses).py):
    (Ping 2 addresses procedurally) 12.183183900022414 seconds

"""
