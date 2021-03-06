import platform
from pathlib import Path

import pytest

# get OS -- currently only working with macOS
operating_platform = platform.platform()

if operating_platform.lower().startswith('darwin'):  # it's macOS
    # assume default install location
    jhove_path = Path.home().joinpath('jhove/jhove')
else:
    # if it's not macOS, but I don't know where to look for jhove yet
    jhove_path = None  # should I just pass here?

image_path = Path.cwd()

def does_jhove_exist(jhove_path=jhove_path):
    return jhove_path.is_file()

jhove_module_list = ['tif', 'tiff', 'jpeg2000']

def jhove(image_path, jhove_module):
    if jhove_module.lower() not in jhove_module_list:
        print(f'jhove_module "{jhove_module}" not in jhove_module_list')
        print(jhove_module_list)
        return

@pytest.mark.skipif(not jhove_path, reason="not macOS, default jhove path unknown")
def test_does_jhove_exist():
    assert does_jhove_exist() == True

@pytest.mark.skipif(does_jhove_exist()==False, reason="jhove not installed in default location")
def test_jhove():
    assert 'tiff' in jhove_module_list
    assert 'TIF' not in jhove_module_list
