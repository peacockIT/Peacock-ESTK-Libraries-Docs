#! /usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#	DESCRIPTION
#
# 	1 *	Builds one single pdf from the whole sphinx documentation

from subprocess import call

# Builds one single pdf from the whole sphinx documentation
def build_sphinx_pdf():
	call("sphinx-build -d 'build pdf/doctrees' -b 'pdf' './source' 'build pdf/pdf'", shell=True, cwd="./docs")

build_sphinx_pdf()


