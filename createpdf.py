#! /usr/bin/env python3
import re
import os
from subprocess import call

SOURCE_FOLDER = './docs/source'
MODULES_FOLDER = './docs/source/modules'

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


# Updates the 'modules' folder and refreshes the docs with 'make html'
def build_pdf():
	print('rst2pdf', RST_FILE, 'result_peacock.pdf')
	call(['rst2pdf', RST_FILE, 'result_peacock.pdf'])

# Updates the 'modules' folder and refreshes the docs with 'make html'
def make_latexpdf():
	call('make latexpdf', shell=True, cwd="./docs")



make_latexpdf()
# build_pdf()

print('Finished creating pdf files')

