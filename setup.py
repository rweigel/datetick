import sys
from setuptools import setup, find_packages

install_requires = ['matplotlib', 'numpy', 'python-dateutil']

setup(
    name='datetick',
    version='0.0.1',
    author='Bob Weigel, Brendan Gallagher',
    author_email='rweigel@gmu.edu',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/datetick/',
    license='LICENSE.txt',
    description='Sensible date tick locator for matplotlib',
#    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=install_requires
)