#!/usr/bin/env python
from setuptools import (setup, find_packages)
import versioneer


setup(name='recordwhat',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      install_requires=['ophyd', 'parsimonious', 'graphviz', 'attrs', 'pandas',
                        'pyepics',
                        ],
      package_data={'recordwhat': ['record_info/*.txt']},
      license='BSD',
      packages=find_packages())
