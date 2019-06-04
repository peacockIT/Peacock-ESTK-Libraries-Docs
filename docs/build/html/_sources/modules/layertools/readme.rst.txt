Peacock Layertools
------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~
Tools for selected Layer/s
~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~
move back
~~~~~~~~~

Moves the selected layer according to the bpm and bars value to the left.

~~~~~~~~~~
move forth
~~~~~~~~~~

Moves the selected layer according to the bpm and bars value to the right.

~~~~~~~~~~~~~~~
Arrange Layer/s
~~~~~~~~~~~~~~~

All selected layers are getting arranged like a stairway according to
the currently set bpm and bars value.

~~~~~~~~~~~~~~~~~~~
Randomize Selection
~~~~~~~~~~~~~~~~~~~

All selected layers are getting randomly deselected.

~~~~~
Foist
~~~~~

For all selected layers:

- The function tries to find a new randomly choosen starttime for the layer

   .. code-block:: javascript

      layer.startTime += (Math.random() < 0.5) ? Math.random() * 100 : Math.random() * -100;

- The function tries to find a new randomly choosen stretch value for the layer

   .. code-block:: javascript

      layer.stretch = 200 * Math.random() or layer.stretch = 200 * Math.random() * (-1)

If the original in- and out-point of the layer have changed by setting
the randomly choosen values

.. code-block:: javascript

   (origInPoint != layer.inPoint && origOutPoint != layer.outPoint)

the function tries to find another starttime/stretch value for the layer
and loops through this process as long as the condition is not true.

