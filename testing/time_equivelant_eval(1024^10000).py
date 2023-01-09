import time

t0 = time.perf_counter()
x = eval('1024**100000')
x = str(x).encode('utf8')
x = eval('1024**100000')
x = str(x).encode('utf8')
x = eval('1024**100000')
x = str(x).encode('utf8')
x = eval('1024**100000')
x = str(x).encode('utf8')
x = eval('1024**100000')
x = str(x).encode('utf8')
x = eval('1024**100000')
x = str(x).encode('utf8')
x = eval('1024**100000')
x = str(x).encode('utf8')
x = eval('1024**100000')
x = str(x).encode('utf8')
print('time taken:', time.perf_counter() - t0)

# (8 operations: 1024**100000) 16.447089799999958 seconds
