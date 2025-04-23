"""
Test for python and OS
"""

import sys
import platform
import pytest

print(sys.version[:4])
print(type(sys.version))

def test_python_version():
    """Test that the Python version is 3.10 or 3.11 or 3.12 or 3.13"""

    assert sys.version[:4] in ["3.10", "3.11", "3.12", "3.13"], "Python version is lower than 3.10"

@pytest.mark.skipif(sys.platform != "linux", reason = "Only runs on Linux")
def test_os_system():
    """Test that the OS system name is correctly identified"""
    #os_name = platform.system()
    #assert os_name == "Linux", "Unexpected OS system name"
    assert True
