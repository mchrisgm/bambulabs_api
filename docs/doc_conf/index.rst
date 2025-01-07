BambuLabs API
=====================================================

Description
===========
API for accessing information for a printer,
including the status of the printer and the status of the print job.


Printer
=======
.. automodule:: bambulabs_api.Printer
  :members:
  :imported-members:

Filament
========
.. automodule:: bambulabs_api.Filament
  :members:
  :imported-members:

AMSFilamentSettings
===================
.. automodule:: bambulabs_api.AMSFilamentSettings
  :members:
  :imported-members:

PrintStatus
===========
.. automodule:: bambulabs_api.PrintStatus
  :members:
  :imported-members:

GcodeState
==========
.. automodule:: bambulabs_api.GcodeState
  :members:
  :imported-members:

Examples
========

Basic
-----

To get started - make sure your printer is on the same network as your target machine.
Make sure that ports 8883, 6000 and 990 are accessible from your machine. 

.. literalinclude:: ../../examples/Basic/basic.py
  :language: python

Basic Subscription
------------------

A simple looping subscription script to get you started once you've been able to connect the printer up to the api.

.. literalinclude:: ../../examples/Basic/basic_subscription.py
  :language: python

Get a Camera Frame
------------------

Access the Camera of a P1 printer:

.. literalinclude:: ../../examples/camera/camera.py
  :language: python

Start a Print
-------------

Start a print using the api given a valid gcode file:

.. literalinclude:: ../../examples/print/print_gcode.py
  :language: python
