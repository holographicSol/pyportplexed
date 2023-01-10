""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import time
import pyportplexed

start_port = 55555
results_port = 12345
n_threads = 8

print('\nStarting Program X: Using PyPortPlexed to compute...')

""" 1. Start daemonic processes with args """
ports = pyportplexed.start(start_port, n_threads, results_port, buffer_size=1024)

""" 2. Connect to daemonic processes """
connections = pyportplexed.connect(ports)

""" 3. Send something for PyPortPlexed to compute """
data = ['1024**100000', '1024**100000', '1024**100000', '1024**100000',
        '1024**100000', '1024**100000', '1024**100000', '1024**100000']
t0 = time.perf_counter()
pyportplexed.send(connections, data=data)

""" 4. Wait for the results to come in from PyPortPlexed """
results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
print('Time taken:', time.perf_counter() - t0)
print('Items in results:', len(results))
print()

""" Repeat. Send more workload(s) to PyPortPlexed """
print('Sending another workload for PyPortPlexed to compute...')
t0 = time.perf_counter()
pyportplexed.send(connections, data=data)
second_results = pyportplexed.results(results_port, n_threads, buffer_size=1024)
print('Time taken:', time.perf_counter() - t0)
print('Items in results:', len(second_results))
print()

""" Destroy the daemonic process(s) when done """
pyportplexed.destroy_daemons(connections)


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
"""
