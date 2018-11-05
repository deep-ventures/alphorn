#!/usr/bin/env python
import os
import re
from setuptools import setup, find_packages

NAME = 'alphorn'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, NAME, 'version.py')) as v_file:
    VERSION = re.compile(r".*__version__ = [\"'](.*?)[\"']", re.S).match(v_file.read()).group(1)

with open('README.md') as readme_file:
    README = readme_file.read()


install_requires = [
]

test_requires = [
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'pylint',
    'autopep8',
]

setup(
    name='alphorn',
    version=VERSION,
    description="AWS Lambda Router Microframework",
    long_description=README,
    author="Thomas Alisi",
    author_email='tom@londondroids.com',
    url='https://github.com/grudelsud/alphorn',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    license="MIT",
    keywords='alphorn lambda aws router',
    test_requires=test_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)
