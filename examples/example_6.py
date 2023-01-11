""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import pyportplexed

spawn_port = 55555
results_port = 12345


def restricting_the_daemon(data=[]):
    """ PyPortPlexed has different daemons that can be leveraged however some are more powerful than others.

    Choose carefully which daemon you wish to use and ultimately compile with.
    Setting restrained=True will force PyPortPlexed to run a restrained version of its daemon that should have
    very restricted access to namespaces.
    The daemons are not imported so one may safely isolate PyPortPlexed from either daemon not being used. Or keep
    them both.
    If you don't need it then do not use it. Make restrained=True to use a less powerful daemon.
    A full list of allowed names can be found in pyportplexed_daemon_restrained.py allowed_names dictionary.
    Restrained variable is False by default. It is up to developers to use a restrained daemon.
    """

    ports = pyportplexed.spawn(spawn_port, int(len(data)), results_port, buffer_size=1024, restrained=True)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=data)
    results = pyportplexed.results(results_port, int(len(data)), buffer_size=1024)
    pyportplexed.destroy_daemons(communions)
    return results


print('Starting Program X: Using PyPortPlexed to compute...')

""" Test allowed names """
_data = ['sum([2,2])',
         'pow(10, 2)',
         'len("foobar")',
         'max([1,2,3,4,5,6,7,8,9])']

""" Test restricted names """
# _data = ['subprocess.getoutput("powershell psexec -w C:/ -i -s cmd")']

""" Test restricted names a different way """
# _data = ['"__import__('subprocess').getoutput('powershell psexec -w C:/ -i -s cmd')", {}, {}']
print(restricting_the_daemon(_data))
