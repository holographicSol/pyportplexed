""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import pyportplexed

spawn_port = 55555
results_port = 12345


def simple_example(data=[]):
    """ An example with different expressions. See eval() documentation.
    """

    communions = pyportplexed.commune(pyportplexed.spawn(spawn_port, int(len(data)), results_port, buffer_size=1024))
    pyportplexed.interface(communions, data=data)
    results = pyportplexed.results(results_port, int(len(data)), buffer_size=1024)

    pyportplexed.destroy_daemons(communions)

    return results


print('Starting Program X: Using PyPortPlexed to compute...')
print(simple_example(data=['50 < 200 and 50 > 100', '150 < 200 and 150 > 100']))
