Peacock ESTK Library Documentation
----------------------------------
It is very important that the ``html`` and ``pdf`` build process is very easy an quick because there will be many modifications to the documentation and it needs to be updated constantly.

In order to make this happen I created 2 python scripts ``build.py`` and ``createpdf.py`` which take care of the whole building process.

By executing ``build.py`` all modules are updated and the html documentation is created. After that is done ``build.py`` executes ``createpdf.py``.

``createpdf.py`` creates a pdf file for each module that is defined in the ``pdf_to_be_created.txt`` file. If that file doesn't exist or it is empty then all modules are getting converted to pdf.

If there are any problems with the rst2pdf package please have a look in the instructions file ``./misc/install_rst2pdf.rst``.


### Sphinx Pdf Creation
First I couldn't get it to work so that I could create one single pdf file from the sphinx documentation.
So here I will document as much as possible to recreate this working scenario next time.

``/Users/danielkreth/python2/lib/python2.7/site-packages/rst2pdf/pdfbuilder.py and .pyc``

Edit config.py
extensions = [ 'rst2pdf.pdfbuilder' ]

``` bash
which python # Should be ~/python2/bin/python

pip install rst2pdf # rst2pdf should be installed: ~/python2/lib/python2.7/site-packages/rst2pdf

```

### rst2pdf Fonts
Install the following otherwise rst2pdf can't find any custom fonts.

``` bash
brew install fontconfig
```

### PDF Styles and Configuration
By default the rst2pdf package is scanning the folder ``~/.rst2pdf`` for a config file and styles.
I created a symbolic link from ``~/.rst2pdf`` to ``~/dotfiles/settings/rst2pdf`` which makes it easy to modify the files and keep it backuped.

The styles for the pdf creation can be found here
``~/dotfiles/settings/rst2pdf/styles/``

These 2 styles I consider my main themes for pdf creation, which are both set as default styles in the config file ``~/dotfiles/settings/rst2pdf/config``.
* ``_peacock_code.style``
* ``_peacock_default.style``


### build.py
1 Replaces the existing 'modules' folder in the docs with the original 'modules' folder from the 'Peacock ESTK Library'
2 Removes the 'lib' folder from each module in the docs so that only the 'readme.rst' remains
3 Rebuilds the docs by calling 'make html'. If option 'clean' is set the build dir is cleaned before rebuilding

### createpdf.py
1 Searches all 'readme.rst' files in './docs/source/modules'
2 Builds one pdf file for each 'readme.rst' file that is defined in the 'pdf_to_be_created.txt' file in './docs/build/pdf/..'