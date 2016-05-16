from setuptools import setup, find_packages

import imp

version = imp.load_source('pysdf.version', 'pysdf/version.py')

setup(
    name='pysdf',
    version=version.version,
    description='Structured Dance Format Schema',
    author='Cinnamon Raisin Developers',
    author_email='christopher.jacoby@gmail.com',
    url='https://github.com/cinnamonraisin/danceschema',
    download_url='',
    packages=find_packages(),
    long_description='',
    classifiers=[
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    keywords='',
    license='ISC',
    install_requires=[
        'joblib',
        'six'
    ],
    extras_require={
        'docs': ['numpydoc']
    }
)
