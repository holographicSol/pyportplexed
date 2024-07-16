# PyPortPlexed

Eval and Exec in the big chair to rule until they will be destroyed.

Essentially PyPortPlexed spawns n daemonic I/O devices that process in parralel
and communicate via ports. Instructions in, Results out.

A working knowledge of eval() is required. eval() is extremely powerful, please use
with caution.

Please understand thoroughly the implications and infinite use cases of eval()
before handing arguments to PyPortPlexed.

When daemons are spawned ensure the very next thing you do is call them. Be the
one who makes the call.

Any daemons spawned should be almost constantly in use otherwise destroy them if
you will not be using them for even around a second. Then make more when you need
them again.

The daemons are networked I/O devices with infinite power thanks and due to eval().

PLEASE: Read through and run the examples so that you can understand everything
current about PyPortPlexed before use. Once some fundamentals are understood,
it is then safe and very simple to use PyPortPlexed.

Locked: receiving data back from eval and exec is restricted to local host but
the restriction can be easily removed, unleashing eval and exec to the entire 
internet for mass distributed compute and control.
