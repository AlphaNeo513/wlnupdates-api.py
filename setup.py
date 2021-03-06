from setuptools import setup, find_packages

with open("README.md", "r") as f:
    readme = f.read()


setup(
    name='wlnupdates',
    version='1.0.6',
    url = 'https://github.com/AlphaNeo513/wlnupdates-api.py',
    python_requires=">= 3.7",
    description='A simple API wrapper for wlnupdates',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='AlphaNeo',
    author_email='sewon360@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['']
)