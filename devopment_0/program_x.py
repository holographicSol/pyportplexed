import time

import module_pyportplexed as th

threads = th.start(55555, 8, 12345)

print('threads:', threads)

connections = th.connect(threads, '1024**100000')

print('connections:', connections)

t0 = time.perf_counter()
results = th.results(12345, 8)
print('time taken:', time.perf_counter() - t0)
print('Items in results:', len(results))

# my pyportplexed (python -OO program_x.py):
# (8 operations: 1024**100000) 2.6084568000005675 seconds

# single thread (python -OO time_equivalent_eval(1024^10000).py):
# (8 operations: 1024**100000) 16.447089799999958 seconds
