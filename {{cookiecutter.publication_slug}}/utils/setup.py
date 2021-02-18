#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
from setuptools import setup, find_packages

from setuptools.command.develop import develop
from setuptools.command.install import install


def set_path_variables():
    print('Setting environment variables...')
    root_dir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

    activate = 'conda activate {}'.format(
        os.path.join(root_dir, 'env', '{{cookiecutter.publication_slug}}'))
    return_code = subprocess.call(activate, shell=True)
    if return_code != 0:
        raise RuntimeError('Could not activate environment.')

    cmd = 'conda env config vars set REPOSITORY_ROOT={}'.format(root_dir)
    return_code = subprocess.call(
        cmd, shell=True)
    if return_code == 0:
        print('The root directory is set to: {}'.format(root_dir))
    else:
        raise RuntimeError(
            'Could not set environment variable. Running "{}" failed'.format(
                cmd))

    return_code = subprocess.call(activate, shell=True)
    if return_code != 0:
        raise RuntimeError('Could not re-activate environment.')


def set_environment_variables(command_subclass):
    """A decorator for classes subclassing one of the setuptools commands.

    It modifies the run() method so that it sets additional environment
    variables inside the conda environment.
    """
    orig_run = command_subclass.run

    def modified_run(self):
        set_path_variables()
        orig_run(self)

    command_subclass.run = modified_run
    return command_subclass


@set_environment_variables
class CustomDevelopCommand(develop):
    pass


@set_environment_variables
class CustomInstallCommand(install):
    pass


setup(
    name='utils',
    version='{{cookiecutter.version}}',
    description='Package for utility functions and data path handling',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    # cmdclass={
    #     'install': CustomInstallCommand,
    #     'develop': CustomDevelopCommand
    # }
)
