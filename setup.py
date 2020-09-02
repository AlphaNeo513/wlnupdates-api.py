from setuptools import setup, find_packages
from wlnupdates import __title__, __author__, __version__

if not __title__:
    raise RuntimeError('title is not set')
if not __author__:
    raise RuntimeError('Author is not set')
if not __version__:
    raise RuntimeError('Version is not set')

with open("README.md", "r") as f:
    readme = f.read()


setup(
    name=__title__,
    version=__version__,
    url = 'https://github.com/AlphaNeo513/wlnupdates-api.py',
    python_requires=">= 3.7",
    description='A simple API wrapper for wlnupdates',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='AlphaNeo',
    author_email='sewon360@gmail.com',
    license='MIT',
     
)