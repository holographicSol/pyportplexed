""" Written by Benjamin Jack Cullen
Intention: Example program using PyPortPlexed.
"""
import time
import pyportplexed
from threading import Thread
from time import sleep

channel_1_results = []
channel_1_data = []

channel_2_results = []
channel_2_data = []

channel_3_results = []
channel_3_data = []

channel_4_results = []
channel_4_data = []


def channel_1():
    """ Provide something for PyPortPlexed to compute on 'channel 1'.
    """
    global channel_1_results, channel_1_data
    channel_1_spawn_port = 55555
    channel_1_results_port = 55550
    n_threads = int(len(channel_1_data))
    ports = pyportplexed.spawn(channel_1_spawn_port, n_threads, channel_1_results_port, buffer_size=1024)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=channel_1_data)
    channel_1_results = pyportplexed.results(channel_1_results_port, n_threads, buffer_size=1024)
    pyportplexed.destroy_daemons(communions)


def channel_2():
    """ Provide something for PyPortPlexed to compute  'channel 2'.
    """
    global channel_2_results, channel_2_data

    channel_2_spawn_port = 55556
    channel_2_results_port = 55551
    n_threads = int(len(channel_2_data))
    ports = pyportplexed.spawn(channel_2_spawn_port, n_threads, channel_2_results_port, buffer_size=1024)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=channel_2_data)
    channel_2_results = pyportplexed.results(channel_2_results_port, n_threads, buffer_size=1024)
    pyportplexed.destroy_daemons(communions)


def channel_3():
    """ Provide something for PyPortPlexed to compute  'channel 2'.
    """
    global channel_3_results, channel_3_data

    channel_3_spawn_port = 55557
    channel_3_results_port = 55552
    n_threads = int(len(channel_3_data))
    ports = pyportplexed.spawn(channel_3_spawn_port, n_threads, channel_3_results_port, buffer_size=1024)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=channel_3_data)
    channel_3_results = pyportplexed.results(channel_3_results_port, n_threads, buffer_size=1024)
    pyportplexed.destroy_daemons(communions)


def channel_4():
    """ Provide something for PyPortPlexed to compute  'channel 2'.
    """
    global channel_4_results, channel_4_data

    channel_4_spawn_port = 55558
    channel_4_results_port = 55553
    n_threads = int(len(channel_4_data))
    ports = pyportplexed.spawn(channel_4_spawn_port, n_threads, channel_4_results_port, buffer_size=1024)
    communions = pyportplexed.commune(ports)
    pyportplexed.interface(communions, data=channel_4_data)
    channel_4_results = pyportplexed.results(channel_4_results_port, n_threads, buffer_size=1024)
    pyportplexed.destroy_daemons(communions)


def channel_master():
    """ Business as usual but with threading.
    This time lets spawn four instances of PyPortPlexed each given instructions and each feeding results back
    into themselves.
    """
    global channel_1_results, channel_1_data
    global channel_2_results, channel_2_data
    global channel_3_results, channel_3_data
    global channel_4_results, channel_4_data

    print('Starting Program X: Using PyPortPlexed to compute...')

    channel_1_data = ['10*1']
    thread = Thread(target=channel_1)
    thread.start()

    channel_2_data = ['10*1']
    thread = Thread(target=channel_2)
    thread.start()

    channel_3_data = ['10*1']
    thread = Thread(target=channel_3)
    thread.start()

    channel_4_data = ['10*1']
    thread = Thread(target=channel_4)
    thread.start()

    channel_1_results_prev = ''
    channel_2_results_prev = ''
    channel_3_results_prev = ''
    channel_4_results_prev = ''
    while '10000000' not in str(channel_4_results):

        if int(len(channel_1_results)) == 1:
            if channel_1_results[0][1] != channel_1_results_prev:
                channel_1_results_prev = channel_1_results[0][1]
                print('channel_1 result:', channel_1_results[0][1])

                if str(channel_1_results[0][1]).isdigit():
                    channel_1_data = [str('10*'+channel_1_results[0][1])]
                    thread = Thread(target=channel_1)
                    thread.start()

        if int(len(channel_2_results) == 1):
            if channel_2_results[0][1] != channel_2_results_prev:
                channel_2_results_prev = channel_2_results[0][1]
                print('channel_2 result:', channel_2_results[0][1])

                if str(channel_2_results[0][1]).isdigit():
                    channel_2_data = [str('10*'+channel_2_results[0][1])]
                    thread = Thread(target=channel_2)
                    thread.start()

        if int(len(channel_3_results)) == 1:
            if channel_3_results[0][1] != channel_3_results_prev:
                channel_3_results_prev = channel_3_results[0][1]
                print('channel_3 result:', channel_3_results[0][1])

                if str(channel_3_results[0][1]).isdigit():
                    channel_3_data = [str('10*'+channel_3_results[0][1])]
                    thread = Thread(target=channel_3)
                    thread.start()

        if int(len(channel_4_results) == 1):
            if channel_4_results[0][1] != channel_4_results_prev:
                channel_4_results_prev = channel_4_results[0][1]
                print('channel_4 result:', channel_4_results[0][1])

                if str(channel_4_results[0][1]).isdigit():
                    channel_4_data = [str('10*'+channel_4_results[0][1])]
                    thread = Thread(target=channel_4)
                    thread.start()

    print('completed.')
    print('')


# uncomment to test
channel_master()
