Peacock BeatManager
-------------------

.. contents:: Table of Contents

~~~~~~~~~~~~
Dependencies
~~~~~~~~~~~~

* Peacock Univarsal Utility :doc:`../utils/readme`
* Peacock AE Utility :doc:`../ae_utils/readme`
* Peacock Preferences :doc:`../preferences/readme`

~~~
Bpm
~~~

Set the bpm rate of the song you want to edit your videos to. Each time
the value is changed a new sliceArray and a new markerArray is created
with slices and markers from 0 to the duration of the active
composition. If no composition is selected slices and markers will be
created from 0 to 60 seconds.

~~~~
Bars
~~~~

Set bars in order to determine how many markers are created when
creating markers. Each time the value is changed a new sliceArray and a
new markerArray is created with slices and markers from 0 to the
duration of the active composition. If no composition is selected slices
and markers will be created from 0 to 60 seconds.