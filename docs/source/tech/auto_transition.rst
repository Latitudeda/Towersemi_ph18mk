auto_transition.py
====================

Define the transition between different waveguide types.

In towersemi_ph18mk PDK, a taper will be added between two waveguides of the same type with different widths and a transition will be added between two waveguides of different types.

Users are allowed to define the taper and set ``DEFAULT`` to their own specific transition policy. Please see ``gpdk > components > transition`` for more examples.