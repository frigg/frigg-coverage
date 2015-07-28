# -*- encoding: utf-8 -*-
import re

from setuptools import setup, find_packages

with open('frigg_coverage/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)

setup(
    name='frigg-coverage',
    version=version,
    description='Coverage report reading util',
    author='The frigg team',
    author_email='hi@frigg.io',
    license='MIT',
    url='https://github.com/frigg/frigg-coverage',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
