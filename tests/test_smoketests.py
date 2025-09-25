import sys
sys.path.append('.')

import bin.normalize as normalize


def test_python_version():
    import sys
    assert sys.version_info.major == 3


def test_os():
    import platform
    assert platform.system() in ["Linux", "Darwin", "Windows"]
