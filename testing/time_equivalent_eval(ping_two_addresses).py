import time
import subprocess

t0 = time.perf_counter()
results = []
ev = eval('subprocess.getoutput("powershell ping 8.8.8.8")')
results.append(ev)
ev = eval('subprocess.getoutput("powershell ping 9.9.9.9")')
results.append(ev)

print('Time taken:', time.perf_counter() - t0)
print('Items in results:', len(results))
