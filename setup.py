from setuptools import setup, find_packages

import version

setup(
    name='template_project',
    # could also get this from version.__author__
    # we don't in case there are multiple committers
    author='Peter Krusche',
    author_email='pkrusche@illumina.com',
    version=version.__version__,
    packages=find_packages('src', exclude=["*.tests"]),
    # This can be used to install scripts system-wide
    # Use with caution.
    # scripts=['bin/runme.py'],
    #
    url='',
    # Pick a license
    license='MIT',
    description='A minimal Python package template project which uses '
                'Sphinx, unit tests and setuptools.',

    # add required packages
    install_requires=[]
)
