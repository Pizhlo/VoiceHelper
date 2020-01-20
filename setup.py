"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ["main.py"]
DATA_FILES = ['/Users/user/PycharmProjects/Helper/main.py--', 'verbose']
OPTIONS = {}

setup(
    name='Helper',
    version='1.0.0',
    packages=[''],
    url='',
    license='',
    author='user',
    author_email='',
    description='', install_requires=['fuzzywuzzy', 'pyttsx3'],
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
