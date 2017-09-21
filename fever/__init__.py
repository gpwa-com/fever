import os
import re

__version__ = '0.1.2'

def version(file):
	"""Return an versioned name of the file."""
	# file = /path/file.ext
	if os.path.exists(file):
		# root = '/path/file'
		# ext = '.ext'
		root, ext = os.path.splitext(file)
		# parentdir = '/path'
		parentdir = os.path.dirname(root)
		# basename = 'file'
		basename = os.path.basename(root)
		# version of the file
		# file (1).ext -> 1, f (2).ext -> 2, ...
		v = _get_version(basename)
		# if we are on version 0, add a space between the ending of the
		# basename of the file and the version number.
		# E.g. file.ext -> file (1).ext
		if v == 0:
			basename = basename + ' '
		# remove any prior version expression (e.g. (1)) from root
		basename = basename.replace('(' + str(v) + ')', '')
		# increment version
		v += 1
		v = '(%d)' % v
		return version(os.path.join(parentdir, basename + v + ext))

	return file

def _get_version(basename):
	"""Returns the version of a file."""
	match = re.search(r"\(\d*\)", os.path.basename(basename))
	if match:
		v = int(match.group(0)
					 .replace('(', '')
					 .replace(')', ''))
		return v

	return 0