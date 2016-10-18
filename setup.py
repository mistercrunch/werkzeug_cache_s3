import os
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
version_string = '0.1.0'

setup(
    name='werkzeug_cache_s3',
    description=("An implementation of werkzeug.contrib.cache for Amazon S3"),
    version=version_string,
    packages=find_packages(),
    install_requires=[
        'boto3>=1.4.1, <2.0',
        'werkzeug>=0.11.11, <1.0',
    ],
    author='Maxime Beauchemin',
    author_email='maximebeauchemin@gmail.com',
    url='https://github.com/airbnb/werkzeug_cache_s3',
    download_url=(
        'https://github.com/airbnb/caravel/tarball/' + version_string),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
