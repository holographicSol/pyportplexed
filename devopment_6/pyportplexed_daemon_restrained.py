""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
           This subprocess should return values back to a program like a thread would but over ports.
Summary: Multiplex via ports.
"""
import socket
import sys

""" Parse sys.argv for input arguments """
port = int(sys.argv[1])
port_1 = int(sys.argv[2])
buffer_size = int(sys.argv[3])

""" Setup socket according to input arguments """
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen()


def eval_expression(input_string):
    # Create a dictionary containing the names that you want to use with eval().
    allowed_names = {"abs": abs,
                     "all": all,
                     "any": any,
                     "ascii": ascii,
                     "bin": bin,
                     "chr": chr,
                     "dir": dir,
                     "divmod": divmod,
                     "hash": hash,
                     "hex": hex,
                     "id": id,
                     "isinstance": isinstance,
                     "iter": iter,
                     "len": len,
                     "max": max,
                     "min": min,
                     "oct": oct,
                     "ord": ord,
                     "pow": pow,
                     "repr": repr,
                     "round": round,
                     "sorted": sorted,
                     "sum": sum
                     }
    # Compile the input string to bytecode using compile() in mode "eval".
    code = compile(input_string, "<string>", "eval")
    # Check .co_names on the bytecode object to make sure it contains only allowed names.
    for name in code.co_names:
        if name not in allowed_names.keys():
            # Raise a NameError if the user tries to enter a name that’s not allowed.
            raise NameError(f"Use of {name} not allowed")

    return eval(code, {"__builtins__": {}}, allowed_names)


""" Create a reusable I/O device in software that communicates over ports """
c = None
con_rcv = ''
while con_rcv != 'terminate':
    con_rcv = ''
    if c is None:

        """ Accept incoming connection """
        c, addr = s.accept()
    else:
        host_ip = s.getsockname()[0]

        """ Allow receive if incoming addr[0] (IP) == socket.getsockname()[0] """
        if host_ip == addr[0]:

            """ Decode the incoming message """
            invocation = bytes(c.recv(buffer_size)).decode('utf8')

            """ Self destruct """
            if invocation != '':
                if invocation == 'terminate':
                    break

                else:
                    """ Do some work, in this example eval() is used statically (test purposes only) CAUTION. """
                    # todo: in this version, restrict eval()s access to namespace
                    # ev = eval(invocation, {"__builtins__": {}}, {})
                    ev = eval_expression(invocation)

                    """ Send the result back to the main program (note: final operation is as client) """
                    s = socket.socket()
                    host = socket.gethostname()
                    s.connect((host, port_1))

                    """ Tag result with port and send it home """
                    s.send(bytes(str(port) + ' ' + str(ev), encoding='utf-8'))
s.close()
