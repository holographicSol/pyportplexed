""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import time
import pyportplexed
from threading import Thread
from time import sleep

spawn_port = 55555
results_port = 12345
threaded_results = []
threaded_data = []


def simple_example_0():
    """ Provide something for PyPortPlexed to compute and then destroy the daemons """

    n_threads = 4

    """ 1. spawn daemonic processes with args """
    ports = pyportplexed.spawn(spawn_port, n_threads, results_port, buffer_size=1024)

    """ 2. commune with daemonic processes """
    communions = pyportplexed.commune(ports)

    data = ['10**1', '10**2', '10**3', '10**4']

    print('Starting Program X: Using PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.interface(communions, data=data)

    """ Wait for the results to come in from PyPortPlexed """
    results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(results))

    """ Destroy the daemonic process(s) when done """
    pyportplexed.destroy_daemons(communions)

    for result in results:
        print('result _id:', result[0], ' result:', result[1])


def simple_example_1():
    """ Provide something for PyPortPlexed to compute and then destroy the daemons """

    n_threads = 8

    """ 1. spawn daemonic processes with args """
    ports = pyportplexed.spawn(spawn_port, n_threads, results_port, buffer_size=1024)

    """ 2. commune with daemonic processes """
    communions = pyportplexed.commune(ports)

    data = ['1024**100000', '1024**100000', '1024**100000', '1024**100000',
            '1024**100000', '1024**100000', '1024**100000', '1024**100000']

    print('Starting Program X: Using PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.interface(communions, data=data)

    """ Wait for the results to come in from PyPortPlexed """
    results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(results))

    """ Destroy the daemonic process(s) when done """
    pyportplexed.destroy_daemons(communions)


def simple_example_2():
    """ Provide something for PyPortPlexed to compute then provide
    PyPortPlexed some more data to compute and then destroy the daemons
    """

    n_threads = 8

    """ 1. spawn daemonic processes with args """
    ports = pyportplexed.spawn(spawn_port, n_threads, results_port, buffer_size=1024)

    """ 2. commune with daemonic processes """
    communions = pyportplexed.commune(ports)

    data = ['1024**100000', '1024**100000', '1024**100000', '1024**100000',
            '1024**100000', '1024**100000', '1024**100000', '1024**100000']

    """ Operation 1. """
    print('Starting Program X: Using PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.interface(communions, data=data)
    results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(results))

    """ Operation 2. """
    print('Providing another workload for PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.interface(communions, data=data)
    second_results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(second_results))

    """ Destroy the daemonic process(s) when done """
    pyportplexed.destroy_daemons(communions)


def simple_example_3():
    """ Provide PyPortPlexed different data to compute
    """

    n_threads = 2

    """ 1. spawn daemonic processes with args """
    ports = pyportplexed.spawn(spawn_port, n_threads, results_port, buffer_size=1024)

    """ 2. commune with daemonic processes """
    communions = pyportplexed.commune(ports)

    data = ['subprocess.getoutput("powershell ping 8.8.8.8")',
            'subprocess.getoutput("powershell ping 9.9.9.9")']

    """ Operation """
    print('Starting Program X: Using PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.interface(communions, data=data)
    results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(results))

    """ Destroy the daemonic process(s) when done """
    pyportplexed.destroy_daemons(communions)


def a_threaded_example_0_A():
    """ Provide something for PyPortPlexed to compute but this time we run this
    function using Python's built in threading so that we have our hands free while
    we PyPortPlex things.
    """
    global threaded_results, threaded_data

    n_threads = 8
    ports = pyportplexed.spawn(spawn_port, n_threads, results_port, buffer_size=1024)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=threaded_data)
    threaded_results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    pyportplexed.destroy_daemons(communions)


def a_threaded_example_0_B():
    """ Business as usual but with threading.
    The same thing can be achieved in infinite ways, like timers or QThreads for example,
    and we implement PyPortPlexed to compute and save time as before.
    """
    global threaded_results, threaded_data

    print('Starting Program X: Using PyPortPlexed to compute...')

    """ Set some data accessible for our function above (a_threaded_example_0_A) """
    threaded_data = ['1024**100000', '1024**100000', '1024**100000', '1024**100000',
                     '1024**100000', '1024**100000', '1024**100000', '1024**100000']

    """ Start the above function (a_threaded_example_0_A) on a thread """
    thread = Thread(target=a_threaded_example_0_A)
    thread.start()

    """ Do other things while PyPortPlexed does n things in parallel! """
    i = 0
    while not threaded_results:
        time.sleep(1)
        i += 1
        print('waiting for PyPortPlexed (super multi-tasking):', i, 'seconds')
    print('Items in results:', len(threaded_results))
    print('')


# uncomment to test
# simple_example_0()
# simple_example_1()
# simple_example_2()
# simple_example_3()
a_threaded_example_0_B()

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
