#! /usr/bin/env python3

import os
from subprocess import call


ORIGINAL_MODULES = '../Peacock-ESTK-Libraries/Peacock ESTK Library/modules'
COPY_MODULES = './docs/source/modules'

if not os.path.exists(ORIGINAL_MODULES):
	print('\nChecking\t folder doesn\'t exist ',ORIGINAL_MODULES)
	exit()
else:
	print('\nChecking\t folder exists ',ORIGINAL_MODULES)



# LIBRARYFOLDERS = ['./docs/source/Peacock ESTK Library/library']
MODULESFOLDERS = ['./docs/source/Peacock ESTK Library/modules']

# OTHER_FOLDERS = ['./', './patches']
# OTHER_FOLDERS = []


# Is not used yet
# def _document_this():
# 	folders = OTHER_FOLDERS
# 	for packagefolder in MODULESFOLDERS:
# 		for folder in os.listdir(packagefolder):
# 			if not folder.startswith("."):
# 				folder = Folder(packagefolder + "/" + folder)
# 				folder.package = "/lib"
# 				folders.append(folder)
# 	return folders



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