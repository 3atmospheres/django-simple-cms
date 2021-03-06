#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='django-simple-cms',
    version='0.3.40',
    description='Simple CMS for your django powered website',
    author='Charles Mastin',
    author_email='c@charlesmastin.com',
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
    install_requires=[
        'django',
        'django-extensions',
        'django-taggit',
        'django-positions',
    ],
)
