auto_link.py
=============

Define the auto link policies between different waveguide type.

For example:

``(type(WG.Strip.C.WIRE_TE) >> type(WG.Strip.C.WIRE_TE), fpt.StraightPrefer(WG.Strip.C.WIRE_TE), fpt.BendUsing(WG.Strip.C.WIRE_TE.BEND_CIRCULAR))``

It means that when the start and end waveguide are both ``WG.Strip.C.WIRE_TE``, the automated waveguide type for routing will be ``WG.Strip.C.WIRE_TE`` and an automated bend ``WG.Strip.C.WIRE_TE.BEND_CIRCULAR`` will be added at a 90 degree turn.


Users are allowed to define and set ``DEFAULT`` to their own specific linking policy.

