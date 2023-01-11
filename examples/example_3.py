""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import pyportplexed

spawn_port = 55555
results_port = 12345


def simple_example(data=[]):
    """ Let's try some different data. Run basically anything n times faster than procedural code. Let's try
    two pings in the time of one.
    """

    communions = pyportplexed.commune(pyportplexed.spawn(spawn_port, int(len(data)), results_port, buffer_size=1024))
    pyportplexed.interface(communions, data=data)
    results = pyportplexed.results(results_port, int(len(data)), buffer_size=1024)

    pyportplexed.destroy_daemons(communions)

    return results


print('Starting Program X: Using PyPortPlexed to compute...')
data = ['subprocess.getoutput("powershell ping 8.8.8.8")',
        'subprocess.getoutput("powershell ping 9.9.9.9")']
print(simple_example(data=data))
