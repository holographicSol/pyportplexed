""" Written by Benjamin Jack Cullen
Intention: This module (to be) distributes workloads to n spawned subprocesses and waits for values to be
           returned.
Summary: Multiplex via ports.
Example program using PyPortPlexed modules.
"""
import time
import module_pyportplexed as th

start_port = 55555
results_port = 12345
n_threads = 8

print('\nStarting Program X: Using PyPortPlexed to compute...')

""" start n_threads processes with args """
threads = th.start(start_port, n_threads, results_port)

""" connect to n_threads processes and give them a workload """
connections = th.connect(threads, '1024**500000')

""" wait for the results to come in from n_threads ports """
t0 = time.perf_counter()
results = th.results(results_port, n_threads)
print('Time taken:', time.perf_counter() - t0)
print('Items in results:', len(results))
print()

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
