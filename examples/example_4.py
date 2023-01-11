""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import time
import pyportplexed
from threading import Thread

spawn_port = 55555
results_port = 12345
results = []
data = []


def simple_example_B():
    """ Provide something for PyPortPlexed to compute but this time we run this
    function using Python's built in threading so that we have our hands free while
    we PyPortPlex things.
    """
    global results, data

    ports = pyportplexed.spawn(spawn_port, int(len(data)), results_port, buffer_size=1024)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=data)
    results = pyportplexed.results(results_port, int(len(data)), buffer_size=1024)
    pyportplexed.destroy_daemons(communions)


def simple_example_A():
    """ Business as usual but with threading.
    The same thing can be achieved in infinite ways, like timers or QThreads for example,
    and we implement PyPortPlexed to compute and save time as before.
    """
    global results
    thread = Thread(target=simple_example_B)
    thread.start()
    i = 0
    while not results:
        time.sleep(1)
        i += 1
        print('waiting for PyPortPlexed (super multi-tasking):', i, 'seconds')
    print('Items in results:', len(results))


print('Starting Program X: Using PyPortPlexed to compute...')
data = ['subprocess.getoutput("powershell ping 8.8.8.8")',
        'subprocess.getoutput("powershell ping 9.9.9.9")']
simple_example_A()
print(results)
