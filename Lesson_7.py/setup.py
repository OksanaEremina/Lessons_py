from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='filesystem_helpers',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
)