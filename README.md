# PyPortPlexed

In early development.

Essentially PyPortPlexed spawns n daemonic I/O devices that process in parralel
and communicate via ports. Instructions in, Results out.

If you left Python for a while to find threads in another language you may come
back home.

PyPortPlexed very simply creates thread like objects that return results via porting
to the n, that can be easily and simply placed directly into a variable made ready to
use with just three lines of code in a Program that imports PyPortPlexed.

A working knwoledge of eval() is required. eval() is extremely powerful, please use
with caution.

Please understand thoroughly the implications and infinite use cases of eval()
before handing arguments to PyPortPlexed.

When daemons are spawned ensure the very next thing you do is call them. Be the
one who makes the call.

Any daemons spawned should be almost constantly in use otherwise destroy them if
you will not be using them for even around a second. Then make more when you need
them again.
