""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import pyportplexed

spawn_port = 55555
results_port = 12345


def simple_example(data=[]):
    """ Same again but this time lets wait before destroying the daemons. However, as soon as we will not be using
    them anymore we will destroy them immediately.
    """

    communions = pyportplexed.commune(pyportplexed.spawn(spawn_port, int(len(data)), results_port, buffer_size=1024))
    pyportplexed.interface(communions, data=data)
    results_0 = pyportplexed.results(results_port, int(len(data)), buffer_size=1024)

    pyportplexed.interface(communions, data=data)
    results_1 = pyportplexed.results(results_port, int(len(data)), buffer_size=1024)

    pyportplexed.destroy_daemons(communions)

    return results_0, results_1


print('Starting Program X: Using PyPortPlexed to compute...')
print(simple_example(data=['10**1', '10**2', '10**3', '10**4', '10**5', '10**6', '10**7', '10**8']))
