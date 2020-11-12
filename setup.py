# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='testing',
    version='0.1',
    description='testing setup',
    author='VJ',
    license='MIT',
    install_requires=[
        'apache-libcloud==3.1.0',
        'docopt==0.6.2',
        'gevent==20.9.0',
        'requests==2.23.0',
        'paramiko==2.4.2',
        'pyyaml>=4.2b1',
    ],
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup']),
)
