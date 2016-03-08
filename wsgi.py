"""
Wrapper for nnscr/wsgi.py that sets the python path.

This will append the current directory and the users site-packages folder to
the include path. Use this if you don't want to configure your WSGI to do this.

If your include path is set correctly, you can also use nnscr/wsgi.py directly.
"""

import os
import sys
import site

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(site.getusersitepackages())

from nnscr.wsgi import application

