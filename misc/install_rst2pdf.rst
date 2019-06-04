
How I've got rst2pdf to work
----------------------------

rst2pdf only works with python2

I always use the virtualenv ``~/python`` which has python3 installed.

.. code-block:: bash
  pip3 install virtualenv
  virtualenv ~/python


Because virtualenv can not have two python versions at once, I created a second virtualenv at ``~/python2``.

.. code-block:: bash
  pip2 install virtualenv
  virtualenv ~/python2


Because I couldn't use pip2 in the firstplace, I had to install python 2 again.
I don't know why but I guess it has to do with the previous pyphon3 and pip3 installation.

.. code-block:: bash
  brew install python@2


In my dotfiles I created 2 aliases to quickly change the virtualenv
mypython, mypython3   -> python3
mypython2             -> python2


Resources
---------

# http://rst2pdf.ralsina.me/handbook.html#styles
# https://github.com/ralsina/rst2pdf/blob/master/README.rst