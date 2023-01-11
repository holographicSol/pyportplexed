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
results_a_threaded_example_1_A = []
threaded_data_a_threaded_example_1_A = []
results_a_threaded_example_2_A = []
threaded_data_a_threaded_example_2_A = []
results_a_threaded_example_2_C = []
threaded_data_a_threaded_example_2_C = []


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
    """ Provide PyPortPlexed different data to compute.
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

    n_threads = 2
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
    threaded_data = ['subprocess.getoutput("powershell ping 8.8.8.8")',
                     'subprocess.getoutput("powershell ping 9.9.9.9")']

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


def a_threaded_example_1_A():
    """ Provide something for PyPortPlexed to compute but this time we make n_threads variable to size of input data.
    """
    global results_a_threaded_example_1_A, threaded_data_a_threaded_example_1_A

    n_threads = int(len(threaded_data_a_threaded_example_1_A))
    ports = pyportplexed.spawn(spawn_port, n_threads, results_port, buffer_size=1024)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=threaded_data_a_threaded_example_1_A)
    results_a_threaded_example_1_A = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    pyportplexed.destroy_daemons(communions)


def a_threaded_example_1_B():
    """ Business as usual but with threading.
    The same thing can be achieved in infinite ways, like timers or QThreads for example,
    and we implement PyPortPlexed to compute and save time as before but this time we let Program X set n_threads
    according to the length of data so that we don't have to manually specify n_threads for each operation containing
    different data quantities.
    """
    global results_a_threaded_example_1_A, threaded_data_a_threaded_example_1_A

    print('Starting Program X: Using PyPortPlexed to compute...')

    threaded_data_a_threaded_example_1_A = ['10**1', '10**2', '10**3', '10**4', '10**5', '10**6', '10**7']
    thread = Thread(target=a_threaded_example_1_A)
    thread.start()
    i = 0
    while not results_a_threaded_example_1_A:
        time.sleep(1)
        i += 1
        print('waiting for PyPortPlexed (super multi-tasking):', i, 'seconds')
    print('Items in results:', len(results_a_threaded_example_1_A))
    print('')


def a_threaded_example_2_A():
    """ Provide something for PyPortPlexed to compute.
    """
    global results_a_threaded_example_2_A, threaded_data_a_threaded_example_2_A

    spawn_port_0 = 55555
    results_port_0 = 12345

    n_threads = int(len(threaded_data_a_threaded_example_2_A))
    ports = pyportplexed.spawn(spawn_port_0, n_threads, results_port_0, buffer_size=1024)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=threaded_data_a_threaded_example_2_A)
    results_a_threaded_example_2_A = pyportplexed.results(results_port_0, n_threads, buffer_size=1024)
    pyportplexed.destroy_daemons(communions)


def a_threaded_example_2_C():
    """ Provide something for PyPortPlexed to compute.
    """
    global results_a_threaded_example_2_C, threaded_data_a_threaded_example_2_C

    spawn_port_1 = 44444
    results_port_1 = 22222

    n_threads = int(len(threaded_data_a_threaded_example_2_C))
    ports = pyportplexed.spawn(spawn_port_1, n_threads, results_port_1, buffer_size=1024)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=threaded_data_a_threaded_example_2_C)
    results_a_threaded_example_2_C = pyportplexed.results(results_port_1, n_threads, buffer_size=1024)
    pyportplexed.destroy_daemons(communions)


def a_threaded_example_2_B():
    """ Business as usual but with threading.
    This time lets spawn two PyPortPlexed operations that we can use independently processing different things and
    again implement threading to keep our hands free while PyPortPlexed parallel computes.
    """
    global results_a_threaded_example_2_A, threaded_data_a_threaded_example_2_A
    global results_a_threaded_example_2_C, threaded_data_a_threaded_example_2_C

    print('Starting Program X: Using PyPortPlexed to compute...')

    threaded_data_a_threaded_example_2_A = ['10**10', '10**20', '10**30', '10**40']
    thread = Thread(target=a_threaded_example_2_A)
    thread.start()

    threaded_data_a_threaded_example_2_C = ['10**1', '10**2', '10**3', '10**4']
    thread = Thread(target=a_threaded_example_2_C)
    thread.start()

    i = 0
    allow_readout_0 = True
    allow_readout_1 = True
    while i < 2:
        if results_a_threaded_example_2_A and allow_readout_0 is True:
            allow_readout_0 = False
            print('Items in first results:', len(results_a_threaded_example_2_A))
            i += 1
        if results_a_threaded_example_2_C and allow_readout_1 is True:
            allow_readout_1 = False
            print('Items in second results:', len(results_a_threaded_example_2_C))
            i += 1
    print('completed.')
    print('')


def restricting_the_daemon():
    """ PyPortPlexed has different daemons that can be leveraged however some are more powerful than others.

    Choose carefully which daemon you wish to use and ultimately compile with.

    Setting restrained=True will force PyPortPlexed to run a restrained version of its daemon that should have
    very restricted access to namespaces.

    If you don't need it then do not use it. Make restrained=True to use a less powerful daemon.

    A full list of allowed names can be found in pyportplexed_daemon_restrained.py allowed_names dictionary.

    Restrained variable is False by default. It is up to developers to use a restrained daemon.
    """

    data = ['sum([2,2])',
            'pow(10, 2)',
            'len("foobar")',
            'max([1,2,3,4,5,6,7,8,9])']

    n_threads = int(len(data))

    """ 1. spawn daemonic processes with args """
    ports = pyportplexed.spawn(spawn_port, n_threads, results_port, buffer_size=1024, restrained=True)

    """ 2. commune with daemonic processes """
    communions = pyportplexed.commune(ports)

    """ Operation """
    print('Starting Program X: Using PyPortPlexed to compute...')
    t0 = time.perf_counter()
    pyportplexed.interface(communions, data=data)
    results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
    print('Time taken:', time.perf_counter() - t0)
    print('Items in results:', len(results))

    """ Destroy the daemonic process(s) when done """
    pyportplexed.destroy_daemons(communions)


# Uncomment to try some infinite possibilities of using PyPortPlexed.

# Example: Simple math across four daemons.
# simple_example_0()

# Example: Simple math across eight daemons.
# simple_example_1()

# Example: Simple math across eight daemons kept alive for more simple math.
# simple_example_2()

# Example: Subprocess a subprocess. Two daemons ping in half the time.
# simple_example_3()

# Example: Threaded ping. Two daemons ping in half the time while program has its hands free.
# a_threaded_example_0_B()

# Example: Dynamic n_thread pertains to list length.
# a_threaded_example_1_B()

# Example: Dual PyPortPlexed.
# a_threaded_example_2_B()

# Example: Restricting the daemon.
restricting_the_daemon()

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
