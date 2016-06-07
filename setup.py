from setuptools import setup
import os
import re


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('./cypher_cossack/__meta__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    version=grep('__version__'),
    name='Cypher Cossack',
    description="",
    packages=[
        'cypher_cossack',
        'cypher_cossack.api',
        'cypher_cossack.tests',
        'cypher_cossack.views',
    ],
    scripts=[
        "bin/manage.py",
    ],
    classifiers=[
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    install_requires=read('dependencies.txt'),
    license="GPLv3",
    zip_safe=False,
)
