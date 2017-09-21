import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import fever.fversioner

def test_save(tmpdir):
	"""Expect to add a version number to a file that already exists."""
	# create a file
	f = tmpdir.join("f.txt")
	f.write('test')
	# check that the file exists
	assert f.check()
	# get the path of the file as a string
	file = os.path.join(f.dirname, 'f.txt')
	# the fversioner.version method should automatically increment filename
	assert fever.fversioner.version(file) == os.path.join(f.dirname, 'f (1).txt')

def test_save_multiple_versions(tmpdir):
	"""Add version number to file if file exists."""
	# create a file
	f = tmpdir.join("f.txt")
	f.write('test')
	f1 = tmpdir.join("f (1).txt")
	f1.write('test')
	# ensure the files exist
	assert f.check()
	assert f1.check()
	# get the path of the file as a string
	file = os.path.join(f.dirname, 'f.txt')
	# the versions.save method should automatically increment filename
	assert fever.fversioner.version(file) == os.path.join(f.dirname, 'f (2).txt')

def test_save_no_prior_versions():
	"""Expect to return the given filename if there is no prior version."""
	# this file doesn't exist
	file = os.path.abspath('./f.txt')
	# the versions.save method should automatically increment filename
	assert fever.fversioner.version(file) == os.path.abspath('./f.txt')

def test_save_parent_dir_has_version_number(tmpdir):
	"""The parent folder should not be impacted by the regex and repalcements"""
	# this file doesn't exist
	f = tmpdir.mkdir('test (1)').join('f.txt')
	f.write("content")
	# check that the file exists
	assert f.check()
	# make a file with the same name
	file = os.path.join(f.dirname, 'f.txt')
	# the versions.save method should automatically increment filename
	assert fever.fversioner.version(file) == os.path.join(f.dirname, 'f (1).txt')

def test_get_version(tmpdir):
	"""Add version number to file if file exists."""
	# create a file

	f = tmpdir.join("f.txt")
	f.write('test')
	f1 = tmpdir.join("f (1).txt")
	f1.write('test')
	# ensure the files exist
	assert f.check()
	assert f1.check()

	root = os.path.join(f1.dirname, f1.purebasename)
	# the versions.save method should automatically increment filename
	assert fever.fversioner._get_version(root) == 1