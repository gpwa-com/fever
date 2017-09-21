from contextlib import contextmanager
import os
import re

__version__ = '0.2.0'


@contextmanager
def fever_open(file, mode='r'):
    f = open(_get_next_version(file), mode)
    try:
        yield f
    finally:
        f.close()


def _get_next_version(file):
    """Return the next version name of the file."""
    # file = /path/file.ext
    if os.path.exists(file):
        # root = '/path/file'
        # ext = '.ext'
        root, ext = os.path.splitext(file)
        # parentdir = '/path'
        parentdir = os.path.dirname(root)
        # basename = 'file'
        basename = os.path.basename(root)
        # _get_next_version of the file
        # file (1).ext -> 1, f (2).ext -> 2, ...
        v = _get_version(basename)
        # if we are on _get_next_version 0, add a space between the ending of the
        # basename of the file and the _get_next_version number.
        # E.g. file.ext -> file (1).ext
        if v == 0:
            basename += ' '
        # remove any prior _get_next_version expression (e.g. (1)) from root
        basename = basename.replace('(' + str(v) + ')', '')
        # increment _get_next_version
        v += 1
        v = '(%d)' % v
        return _get_next_version(os.path.join(parentdir, basename + v + ext))

    return file


def _get_version(basename):
    """Returns the _get_next_version of a file."""
    match = re.search(r"\(\d*\)", basename)
    if match:
        v = int(match.group(0)
                .replace('(', '')
                .replace(')', ''))
        return v

    return 0
