#!/usr/bin/env python

import sys

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages, Command

setup(
    name='django-simple-cms',
    version='0.1.1',
    description='Simple CMS for your django powered website',
    author='Charles Mastin',
    author_email='charles@bricksf.com',
    url='https://github.com/charlesmastin/django-simple-cms/',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
    zip_safe=False,
    dependency_links = [
        'https://github.com/jpwatts/django-positions/tarball/master#egg=django-positions',
    ],
    install_requires=[
        'django',
        'django-extensions',
        'django-taggit',
        'PIL',
        'django-positions',
    ],
)
