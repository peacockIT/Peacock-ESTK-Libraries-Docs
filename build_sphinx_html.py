#! /usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#	DESCRIPTION
#
# 	1 *	Replaces the existing 'modules' folder in the docs with the
#		original 'modules' folder from the 'Peacock ESTK Library'
#
# 	2 * Removes the 'lib' folder from each module in the docs so
#		that only the 'readme.rst' remains
#
# 	3 * Rebuilds the docs by calling 'make html'.
#		If option 'clean' is set the build dir is cleaned before
#		rebuilding
#

import os
from subprocess import call



# Updates the 'modules' folder and refreshes the docs with 'make html'
def build_sphinx():
	print('Creating\t html')
	call('make html', shell=True, cwd="./docs")


# Builds one single pdf from the whole sphinx documentation
def build_sphinx_pdf():
	call("sphinx-build -d 'build pdf/doctrees' -b 'pdf' './source' 'build pdf/pdf'", shell=True, cwd="./docs")

# Builds the docs with options
def docbuild(part='all'):
	if part == 'project':
		build_sphinx()
	elif part == 'clean':
		print('Cleaning\t./docs/build/')
		call('make clean', shell=True, cwd="./docs")
		print('')
		build_sphinx()
	else:
		build_sphinx()


# Build
def build():
	docbuild('clean')




build()


