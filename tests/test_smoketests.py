import sys
import platform

sys.path.append('.')
import bin.normalize as normalize


def test_python_version():
    import sys
    assert sys.version_info.major == 3

def test_os_any():
    import platform
    assert platform.system() in ["Linux", "Darwin", "Windows"]

def test_python_version():
    # Only pass for Python 3.12 or 3.13
    assert sys.version_info[:2] in [(3, 12), (3, 13)]
    
def test_os():
    # Only pass for Linux
    assert platform.system() == "Linux"
