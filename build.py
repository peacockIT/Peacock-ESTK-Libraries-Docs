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


ORIGINAL_MODULES = '../Peacock-ESTK-Libraries/Peacock ESTK Library/modules'
COPY_MODULES = './docs/source/modules'

if not os.path.exists(ORIGINAL_MODULES):
	print('\nChecking\t folder doesn\'t exist ',ORIGINAL_MODULES)
	exit()
else:
	print('\nChecking\t folder exists ',ORIGINAL_MODULES)

MODULESFOLDERS = ['./docs/source/modules']


# Replaces the existing 'modules' folder in the docs with the original 'modules' folder from the 'Peacock ESTK Library'
# 	* Replaces the existing 'modules' with the original 'modules'
# 	* Removes the 'lib' folder from each module so that only the 'readme.rst' remains
def copyModules():
	print('Removing\t', COPY_MODULES)
	call(['rm', '-r', COPY_MODULES])
	print('Copying\t\t', ORIGINAL_MODULES, ' -> ', COPY_MODULES)
	call(['cp', '-a', ORIGINAL_MODULES, COPY_MODULES])

	for root, dirs, files in os.walk(COPY_MODULES):
		for name in dirs:
			if os.path.basename(name) == 'lib':
				print('Removing\t', os.path.join(root, name))
				call(['rm', '-r', os.path.abspath(os.path.join(root, name))])


# Updates the 'modules' folder and refreshes the docs with 'make html'
def build_sphinx():
	copyModules()
	print('Creating\t html')
	call('make html', shell=True, cwd="./docs")



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


call(['./createpdf.py'])


