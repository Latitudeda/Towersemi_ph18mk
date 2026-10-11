PDK structure
======================

Process Design Kit (PDK) is a tool for designated users to generate circuit layouts based on Tower Semiconductor design rules and technology settings.

``towersemi_ph18mk`` package includes five subfolders: ``components``, ``examples``, ``schematic``, ``symbols`` and ``technology``.

* ``components``

    * Fixed cells: All fixed cells, including ``Cross``, ``Directional Coupler``, ``Grating Coupler``, ``MultiMode Interferometer``, ``Phase Shifter``, ``Photodiode``, ``S bend``, ``Towersemi_bend``, ``Towersemi_taper``, ``Y junction``, ``Transition`` and ``Towersemi_wg`` are named and designed by **Tower Semiconductor** and cannot be changed.

    * Parametrized cells (PCells): Designed by **LDS**, including ``Bend``, ``Straight``, ``Bond Pad`` and ``Taper``. Please see ``gpdk > components`` for more designed components by **LDS**.

* ``examples``

    * ``tech_demo.py`` : Test that waveguide types, metal wire types, auto routing, auto link and auto vias function work normally under the PDK setting. Please see ``gpdk > examples`` for more circuit examples.

* ``schematic``

    * Store the schematic setting for linking PhotoCAD to AdvancedSDL.

* ``symbols``

    * Store the symbol setting for linking PhotoCAD to AdvancedSDL.

* ``technology``

    * Store the technology setting which matched the Tower Semiconductor design rules. We recommend users not to change the settings in technology folder.

    * See chapter ``Technology setting`` for more specific definition.

* ``towersemi_ph18mk.lyp`` : This file allows layout tools e.g. KLayout to recognize the layer information when displaying gds file to the layout tool.

    .. image:: ../images/lyp.png
