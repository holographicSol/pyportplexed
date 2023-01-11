""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import time
import pyportplexed

spawn_port = 55555
results_port = 12345


def simple_example(data=[]):
    """ Provide something for PyPortPlexed to compute and then destroy the daemons and return results."""

    n_threads = int(len(data))

    """ 1. spawn daemonic processes with args """
    ports = pyportplexed.spawn(spawn_port, n_threads, results_port, buffer_size=1024)

    """ 2. commune with daemonic processes """
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
