#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
# vim: set et ts=4 sw=4:
'''
  mdbook-pdf-outline
  Author:  Hollow Man <hollowman@opensuse.org>

  Copyright © 2022 Hollow Man(@HollowMan6). All rights reserved.

  This document is free software; you can redistribute it and/or modify it under the terms of the GNU General
  Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option)
  any later version.
'''

from setuptools import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='mdbook-pdf-outline',
      version='0.1.0',
      description='Tool for generating outlines for PDF files generated by mdbook-pdf.',
      url='https://github.com/HollowMan6/mdbook-pdf',
      author='Hollow Man (Domain Address)',
      author_email='hollowman@opensuse.org',
      license='GPL-3.0-or-later',
      install_requires=['lxml', 'pypdf'],
      packages=['mdbook_pdf_outline'],
      entry_points={'console_scripts': [
          'mdbook-pdf-outline=mdbook_pdf_outline.mdbook_pdf_outline:main']},
      long_description=long_description,
      project_urls={
          "Bug Tracker": "https://github.com/HollowMan6/mdbook-pdf/issues",
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Topic :: Text Processing :: Markup :: Markdown",
      ],
      long_description_content_type='text/markdown'
      )