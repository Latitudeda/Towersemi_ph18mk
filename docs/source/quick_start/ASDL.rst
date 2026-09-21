AdvancedSDL
=======================================

Import Tower_PH18MK_PDK into AdvancedSDL
***************************************************************************************

Click ``PDK`` on the top toolbar of **AdvancedSDL** and select ``Open PDK Symbol Design``.

.. image:: ../images/ASDL_1.png

Locate and select the ``towersemi_ph18mk`` folder.

.. image:: ../images/ASDL_2.png

After the import is complete, you will see the ``towersemi_ph18mk`` component library on the left.

.. image:: ../images/ASDL_3.png

Click ``File`` and then click ``New Project``.

.. image:: ../images/ASDL_4.png

Enter the project name and path, select ``towersemi_ph18mk`` in the PDK column, and click ``OK``.

.. image:: ../images/ASDL_5.png

Wait for the contents of ``Import towersemi_ph18mk PDK symbols succeeded`` to appear in the output.

.. image:: ../images/ASDL_6.png

Drag components to the center region.

.. image:: ../images/ASDL_8.png

Click on the component, the parameters of the component can be adjusted on the right side.

.. image:: ../images/ASDL_9.png

Once the parameters are set, connect the ports to route the components and click SDL in the upper right.

.. image:: ../images/ASDL_10.png

The corresponding layout is displayed in the ``Layout View``.

.. image:: ../images/ASDL_11.png

The script generated in the lower left can also be run in **PhotoCAD** and modified to create a new layout. The script is saved in the project's Temp folder.

.. image:: ../images/ASDL_12.png

You can also easily import a specific component to **AdvancedSDL** on **PhotoCAD** using ``fp.export_schematic``. See ``gpdk > examples`` for more information.