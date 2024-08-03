from setuptools import setup

setup (name = 'vc',
       version = '1.0',
       packages = ['vc'],
       entry_points = {
           'console_scripts' : [
               'vc = vc.cli:main'
           ]
       })