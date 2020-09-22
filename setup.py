#!/usr/bin/env python
"""A Nose plugin to support IPython doctests.
"""

from setuptools import setup, find_packages
from glob import glob
from os import path


setup(name='flask_fastful',
      version='0.1',
      author='daniel',
      description = 'flask scaffold init tool, some utils for flask restful api',
      license = '',
      include_package_data=True,
      packages = [
        'flask_fastful',
        'flask_fastful.utils',
        'flask_fastful.commands',
        'flask_fastful.templates',
        ],
      package_data = {
        'flask_fastful.templates': ['project_templates/*.py'],
        '': ["*.py", "*.py-tpl"],
        },
      scripts=['scripts/flask_fastful'],
      platforms="any",
      install_requires = ["flask_restful"],
      entry_points = {
        },
      )
