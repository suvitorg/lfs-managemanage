# -*- coding: utf-8 -
#
# This file is part of lfs-managemanage released under the MIT license. 
# See the NOTICE for more information.

import os
import sys
from setuptools import setup, find_packages

from lfs_managemanage import VERSION


setup(
    name='lfs_managemanage',
    version=VERSION,

    description='Manage of LFS manage interface by javascript and css',
    long_description=file(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    author='Victor Safronovich (suvit)',
    author_email='vsafronovich@gmail.com',
    license='MIT',
    url='http://github.com/suvit/lfs-managemanage',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=['django-appconf',
    ],
    include_package_data=True,
)
