from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fever',
    version='0.1.0',
    description='Automatic file versioning',
    long_description=readme,
    author='Zachary Luety',
    author_email='zluety@gmail.com',
    url='https://github.com/zrluety/fever',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)