""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import time
import pyportplexed

spawn_port = 55555
results_port = 12345


def simple_example(data=[]):
    """ Provide something for PyPortPlexed to compute and then destroy the daemons and return results.

    Note: For this example to work, ports 55555 to 55558 must be free because len(data) is 4, which means PyPortPlexed
          will spawn 4 daemons that will try to provide I/O on ports 55555 to 55558.
          Bear this strongly in mind when using PyPortPlexed.
    """

    n_threads = int(len(data))

    """ 1. Spawn daemonic processes with args """
    ports = pyportplexed.spawn(spawn_port, n_threads, results_port, buffer_size=1024)

    """ 2. Commune with daemonic processes """
    communions = pyportplexed.commune(ports)

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
    return results


print(simple_example(data=['10**1', '10**2', '10**3', '10**4']))
