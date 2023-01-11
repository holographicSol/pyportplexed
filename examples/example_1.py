""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import pyportplexed

spawn_port = 55555
results_port = 12345


def simple_example(data=[]):
    """ Same as example_0 but this time demonstrating how much can be done in just a few lines before all
    results get slam-dunked back into our results variable from any logical number of daemons. Clean.
    """

    communions = pyportplexed.commune(pyportplexed.spawn(spawn_port, int(len(data)), results_port, buffer_size=1024))
    pyportplexed.interface(communions, data=data)
    results = pyportplexed.results(results_port, int(len(data)), buffer_size=1024)

    pyportplexed.destroy_daemons(communions)

    return results


print('Starting Program X: Using PyPortPlexed to compute...')
print(simple_example(data=['10**1', '10**2', '10**3', '10**4', '10**5', '10**6', '10**7', '10**8']))
