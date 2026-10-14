auto_vias.py
====================

Define the vias between different metal line types.

In towersemi_ph18mk PDK, the vias array of the ``via1`` layer will be added when the connection is made between the metal lines of the ``metal1`` layer and the ``metal2`` layer. Accordingly, the metal lines on the ``metal2`` layer and the ``metal3`` layer will be connected via the ``via2`` layer.

Users are allowed to define vias and change related parameters by their own specific requirements. Please see ``technology > vias.py`` and ``components > via > vias.py`` to modify the default vias. Please note that the structure of the vias needs to follow the design rules of **Tower**.
