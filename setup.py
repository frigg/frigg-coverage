# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='frigg-coverage',
    version='1.1.0',
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
