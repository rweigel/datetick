"""Tox test startup customization for Windows DLL resolution.

This module is auto-imported by Python during startup when present on
PYTHONPATH. It ensures native extension dependencies in tox environments
are discoverable before importing packages like matplotlib.

Can be removed when Python 3.11+ is the minimum supported version
"""

import os
import sys


if os.name == "nt":
    dll_dirs = [
        sys.prefix,
        os.path.join(sys.prefix, "Scripts"),
        os.path.join(sys.prefix, "Library", "bin"),
    ]

    add_dll_directory = getattr(os, "add_dll_directory", None)
    if add_dll_directory is not None:
        for dll_dir in dll_dirs:
            if os.path.isdir(dll_dir):
                try:
                    add_dll_directory(dll_dir)
                except OSError:
                    pass

    existing_path = os.environ.get("PATH", "")
    prepend = [dll_dir for dll_dir in dll_dirs if os.path.isdir(dll_dir)]
    if prepend:
        os.environ["PATH"] = os.pathsep.join(prepend + [existing_path])
