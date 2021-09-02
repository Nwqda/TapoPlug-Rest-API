'''
Build script for Tapo PluG API
'''

from setuptools import setup
from codecs import open
from os import path
import tapo_plug

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="tapo_plug",
      packages=["tapo_plug"],
      version=tapo_plug.__version__,
      include_package_data=True,
      exclude_package_data={'': ['*.pyc']},
      author="Samy Younsi (Naqwada)",
      author_email="naqwada@pm.me",
      url="https://gitlab.com/Naqwada/TapoPlug-Rest-API",
      include_dirs=["."],
      license='MIT',
      description="A REST API warper for TP-Link Tapo P100/P105.",
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License"
      ],
      keywords="TP_LINK, tapo, smart plug, iot, p100, p105",
      install_requires=['requests >= 1.4', 'Crypto', 'pkcs7', ])
