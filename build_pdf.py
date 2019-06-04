#! /usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#	DESCRIPTION
#
#	1 * Searches all 'readme.rst' files in './docs/source/modules'
#
#	2 * Builds one pdf file for each 'readme.rst' file that is defined in the 'pdf_to_be_created.txt' file in
#		'./docs/build/pdf/..'
#
#	OPTION
#		* modifyConfig()
#			Iterates all lines of the config file and modifies the
#			line 'stylesheets="[STYLE]"' by replacing the current style.
#
#		* build_pdf_iterate()
#			Updates the 'modules' folder and refreshes the docs with 'make html'
#
#
#		* getListFromTxtFile()
#			Reads a .txt file and creates an array of strings of all lines that doesn't include '#' or nothing
#
#
#		* createJson()
#			Not used
#
#
#		* readJson()
#			Not used
#

import re
import os
from subprocess import call
import json

SOURCE_FOLDER = './docs/source'
MODULES_FOLDER = './docs/source/modules'

# PDF_OUT = './docs/build/pdf'
PDF_OUT = 'pdf'

try:
	os.mkdir(PDF_OUT)
except OSError:
	print ("Directory %s already exists" % PDF_OUT)
else:
	print ("Successfully created the directory %s " % PDF_OUT)


TXT_FILE = 'pdf_to_be_created.txt'

RST_FILE = SOURCE_FOLDER+'/index.rst'
RST_FILE = MODULES_FOLDER+'/console/readme.rst'

CONFIG_FILE = os.path.expanduser('~/dotfiles/settings/rst2pdf/config')

# Iterates all lines of the config file and inserts the line 'stylesheets="[STYLE]"' an new style
def modifyConfig(style):
	with open(CONFIG_FILE) as f:
		new_string = ''
		for l in f:
			line = re.sub('\n', '', l)
			if len(line) > 0 and line[0] != '#' and re.search('stylesheets',line) != None:
				# print(re.sub(line))
				print(line)
				new_string += 'stylesheets="'+style+'"\n'
			else:
				new_string += line + '\n'
		# old = f.read()

	with open(CONFIG_FILE, "w") as f:
		# f.seek(0)
		f.write(new_string)


# Updates the 'modules' folder and refreshes the docs with 'make html'
def build_pdf_iterate():
	code_styles = ['code_default', 'code_autumn', 'code_borland', 'code_bw', 'code_colorful', 'code_emacs', 'code_friendly', 'code_manni', 'code_murphy', 'code_native', 'code_pastie', 'code_perldoc', 'code_trac', 'code_vs']
	for style in code_styles:
		modifyConfig(style)
		print('rst2pdf', RST_FILE, 'result_'+style+'.pdf')
		call(['rst2pdf', RST_FILE, 'result_'+style+'.pdf'])
		# call('rst2pdf '+RST_FILE+' result_'+style+'.pdf -s '+style)


def getListFromTxtFile(file):
	module_list = []
	with open(file) as f:
		for l in f:
			line = re.sub('\n', '', l)
			if len(line) > 0 and line[0] != '#':
				module_list.append(line)
	return module_list



def createJson(data, file):
	data = {}
	data['people'] = []
	data['people'].append({
		'name': 'Scott',
		'website': 'stackabuse.com',
		'from': 'Nebraska'
	})
	with open(file, 'w') as outfile:
		json.dump(data, outfile, sort_keys=True, indent=4)
		data = json.dumps(data, sort_keys=True, indent=4)



def readJson(file):
	with open(file) as json_file:
		data = json.load(json_file)
		for p in data['people']:
			print('Name: ' + p['name'])
			print('Website: ' + p['website'])
			print('From: ' + p['from'])
			print('')



# Updates the 'modules' folder and refreshes the docs with 'make html'
def build_pdf():
	exists = os.path.isfile(TXT_FILE)
	if exists:
		module_list = getListFromTxtFile(TXT_FILE)
	else:
		module_list = []
		f = open(TXT_FILE,"w+")
		f.write("# USAGE\n# This .txt file determines which modules are converted to pdf when executing the script 'createpdf.py'\n# The output path is ./docs/build/pdf/..\n\n")
	counter = 1
	for root, dirs, files in os.walk(MODULES_FOLDER):
		for file in files:
			if file == 'readme.rst':
				NAME = os.path.basename(root)
				PATH = os.path.join(root, file)

				if NAME in module_list or len(module_list) == 0:
					print('rst2pdf', PATH, PDF_OUT+'/peacock_'+NAME+'.pdf')
					call(['rst2pdf', PATH, PDF_OUT+'/peacock_'+NAME+'.pdf'])
					if not exists:
						f.write(NAME+'\n')
					counter+=1




# Updates the 'modules' folder and refreshes the docs with 'make html'
def make_latexpdf():
	call('make latexpdf', shell=True, cwd="./docs")



# make_latexpdf()
build_pdf()

print('Finished creating pdf files')

