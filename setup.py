#!/usr/bin/env python
from setuptools import find_packages, setup

from djangocms_style import __version__

REQUIREMENTS = [
    "django-cms>=3.7",
    "djangocms-attributes-field>=1",
]


CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Framework :: Django",
    "Framework :: Django :: 3.2",
    "Framework :: Django :: 4.0",
    "Framework :: Django :: 4.1",
    "Framework :: Django :: 4.2",
    "Framework :: Django CMS",
    "Framework :: Django CMS :: 3.7",
    "Framework :: Django CMS :: 3.8",
    "Framework :: Django CMS :: 3.9",
    "Framework :: Django CMS :: 3.10",
    "Framework :: Django CMS :: 3.11",
    "Framework :: Django CMS :: 4.1",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
]


setup(
    name="djangocms-style",
    version=__version__,
    author="Divio AG",
    author_email="info@divio.ch",
    maintainer="Django CMS Association and contributors",
    maintainer_email="info@django-cms.org",
    url="https://github.com/django-cms/djangocms-style",
    license="BSD-3-Clause",
    description="Adds style plugin to django CMS",
    long_description=open("README.rst").read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite="tests.settings.run",
)
