# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='hardware_details',
    version='0.1',
    description='Gets the hardware details for servers',
    author='VJ',
    author_email='vavuthu@redhat.com',
    license='MIT',
    install_requires=[
        'apache-libcloud',
        'docopt==0.6.2',
        'gevent==1.4.0',
        'reportportal-client<4.0.0',
        'requests==2.21.0',
        'paramiko==2.4.2',
        'pyyaml>=4.2b1',
        'jinja2==2.10.1',
        'kubernetes==10.0.1',  # latest openshift requires this version
        'openshift',
        'boto3',
        'munch',
        'pytest==5.3.5',
        'pytest-reportportal==1.0.5',
        'pytest-logger',
        'dataclasses',  # For compatibility with python 3.6
        'pytest-html',
        'bs4',
        'gspread',
        'oauth2client',
        'pytest_marker_bugzilla>=0.9.3',
        'pyvmomi',
        'pyhcl',
        # issue opened for botocore
        # https://github.com/boto/botocore/issues/1872
        # till above issue fixed, manually pointing python-dateutil to 2.8.0
        'python-dateutil==2.8.0',
        'pytest-ordering',
        'funcy',
        'semantic-version',
        'jsonschema>=3.2.0',
    ],
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup']),
)

