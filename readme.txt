#####################
### build
#####################
#	1 * Copy modules from Peacock ESTK Library
#		./copy_modules.py
#
#	2 * Copy scripts from the SCRIPTS folder ...
#			/SCRIPTS/sync_scripts_with_docs.py
#
#	3 * Building sphinx html ...
#		./build_sphinx_html.py
#
#	4 * Building sphinx pdf ...
#		./build_sphinx_pdf.py
#
#	5 * Building pdf files for modules ...
#		./build_pdf.py

#####################
### build_html
#####################
#	1 * Copy modules from Peacock ESTK Library ...
#		./copy_modules.py
#
#	2 * Building sphinx html ...
#		./build_sphinx_html.py

#####################
### build_pdf
#####################
#	1 * Copy modules from Peacock ESTK Library ...
#		./copy_modules.py

#	2 * Building pdf files for modules ...
#		./build_pdf.py

#####################
### build_pdf.py
#####################

#	1 * Searches all 'readme.rst' files in './docs/source/modules'
#
#	2 * Builds one pdf file for each 'readme.rst' file that is defined in the 'pdf_to_be_created.txt' file in
#		'./docs/build/pdf/..'

#####################
### build_sphinx_html.py
#####################
# 	1 *	Replaces the existing 'modules' folder in the docs with the
#		original 'modules' folder from the 'Peacock ESTK Library'
#
# 	2 * Removes the 'lib' folder from each module in the docs so
#		that only the 'readme.rst' remains
#
# 	3 * Rebuilds the docs by calling 'make html'.
#		If option 'clean' is set the build dir is cleaned before
#		rebuilding

#####################
### build_sphinx_pdf.py
#####################
# 	1 *	Builds one single pdf from the whole sphinx documentation


#####################
### copy_modules.py
#####################
# 	1 *	Replaces the existing 'modules' folder in the docs with the
#		original 'modules' folder from the 'Peacock ESTK Library'
#

#####################
### pdf_to_be_created.txt
#####################
#	This .txt file determines which modules are converted to pdf when executing the script 'createpdf.py'
#	The output path is .pdf/..

#####################
### push
#####################
#	git add .;
#	git commit -m "work in progress";
#	git push origin develop;
