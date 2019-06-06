Peacock Color Presets
---------------------

~~~~~~~~~~~~
Dependencies
~~~~~~~~~~~~

* Peacock Preferences :doc:`../preferences/readme`


Extend the functionality of the preferences as follows

.. code-block:: javascript

  JsonPreferences.prototype.getColor = function(index){
      if(this.get('defaultColors')[index] == undefined) return null;
      return this.get('defaultColors')[index];
  }

  JsonPreferences.prototype.setColor = function(color, index){
      var colors = this.get('defaultColors');
      colors[index] = color;
      this.set('defaultColors', colors);
  }