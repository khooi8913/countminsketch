from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='countminsketch',
    version='0.1.0',
    description='Count-Min Sketch implementation,
    long_description=readme,
    author='Peter Xenopoulos',
    author_email='xenopoulos@nyu.edu',
    url='https://github.com/pnxenopoulos/countminsketch',
    license=license
)
