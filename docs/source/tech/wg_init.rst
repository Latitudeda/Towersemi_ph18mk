__init__.py
===================

Define the WG class which consists of ``Strip.C.WIRE_TE``, ``Strip.C.WIRE_TM``, ``Strip.O.WIRE_TE``, ``Strip.O.WIRE_TM``, ``Ridge.C.WIRE_TE``, ``Ridge.C.WIRE_TM``, ``Ridge.O.WIRE_TE``, ``Ridge.O.WIRE_TM``, ``SiN_strip.C.WIRE_TE``, ``SiN_strip.C.WIRE_TM``, ``SiN_strip.O.WIRE_TE`` and ``SiN_strip.O.WIRE_TM`` classes. For the towersemi_ph18mk PDK, the WG class additionally includes ``RidgeNitride.C.WIRE_TE``, ``RidgeNitride.C.WIRE_TM``, ``RidgeNitride.O.WIRE_TE``, ``RidgeNitride.O.WIRE_TM``, ``SiN2_strip.C.WIRE_TE``, ``SiN2_strip.C.WIRE_TM``, ``SiN2_strip.O.WIRE_TE``, ``SiN2_strip.O.WIRE_TM``, ``SiN3_strip.C.WIRE_TE``, ``SiN3_strip.C.WIRE_TM``, ``SiN3_strip.O.WIRE_TE`` and ``SiN3_strip.O.WIRE_TM`` classes. The width of the waveguide is set here according to the parameters in ``constant.py`` file. **PhotoCAD** also supports CD bias control of the waveguide width. The CD bias setting can be implemented in ``strip.py``, ``ridge.py``, ``SiN_strip.py``, ``ridgenitride.py``, ``SiN2_strip.py`` and ``SiN3_strip.py``.

.. table:: Waveguide Type Table

    ================================  ==========================================
    WAVEGUIDE_TYPE                    PARAMETERS
    ================================  ==========================================
    `TECH.WG.Strip.C.WIRE_TE`         core_width=0.4500
    `TECH.WG.Strip.C.WIRE_TM`         core_width=0.4500
    `TECH.WG.Strip.O.WIRE_TE`         core_width=0.4000
    `TECH.WG.Strip.O.WIRE_TM`         core_width=0.4000
    `TECH.WG.Ridge.C.WIRE_TE`         core_width=0.4500, cladding_width=4.4500
    `TECH.WG.Ridge.C.WIRE_TM`         core_width=0.4500, cladding_width=4.4500
    `TECH.WG.Ridge.O.WIRE_TE`         core_width=0.4500, cladding_width=4.4500
    `TECH.WG.Ridge.O.WIRE_TM`         core_width=0.4500, cladding_width=4.4500
    `TECH.WG.SiN_strip.C.WIRE_TE`     core_width=0.7000
    `TECH.WG.SiN_strip.C.WIRE_TM`     core_width=0.8000
    `TECH.WG.SiN_strip.O.WIRE_TE`     core_width=0.7000
    `TECH.WG.SiN_strip.O.WIRE_TM`     core_width=0.7000
    ================================  ==========================================

.. table:: Additional Waveguide Type Table

    ===================================  ==========================================================
    WAVEGUIDE_TYPE                       PARAMETERS
    ===================================  ==========================================================
    `TECH.WG.RidgeNitride.C.WIRE_TE`      core_width=0.9000, cladding_width=2.4000, overlap=0.2000
    `TECH.WG.RidgeNitride.C.WIRE_TM`      core_width=0.9000, cladding_width=2.4000, overlap=0.2000
    `TECH.WG.RidgeNitride.O.WIRE_TE`      core_width=0.9000, cladding_width=2.4000, overlap=0.2000
    `TECH.WG.RidgeNitride.O.WIRE_TM`      core_width=0.9000, cladding_width=2.4000, overlap=0.2000
    `TECH.WG.SiN2_strip.C.WIRE_TE`        core_width=0.7000
    `TECH.WG.SiN2_strip.C.WIRE_TM`        core_width=0.7000
    `TECH.WG.SiN2_strip.O.WIRE_TE`        core_width=0.7000
    `TECH.WG.SiN2_strip.O.WIRE_TM`        core_width=0.7000
    `TECH.WG.SiN3_strip.C.WIRE_TE`        core_width=0.7000
    `TECH.WG.SiN3_strip.C.WIRE_TM`        core_width=0.7000
    `TECH.WG.SiN3_strip.O.WIRE_TE`        core_width=0.7000
    `TECH.WG.SiN3_strip.O.WIRE_TM`        core_width=0.7000
    ===================================  ==========================================================

