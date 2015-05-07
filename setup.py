from setuptools import setup, find_packages

setup(
    name='dogebuild-fpc',
    version='0.1',
    description='Free Pascal Compiler plugin for dogebuild',
    author='Kirill Sulim',
    author_email='kirillsulim@gmail.com',
    url='https://github.com/dogebuild/fpc',
    packages=find_packages(include=[
        'dogebuild*',
      ]),
)
