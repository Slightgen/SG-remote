#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


setup(
    name='SG-remote',
    version='1.0.0',
    url='https://github.com/girish946/SG-remote',
    author='girish joshi',
    author_email='girish946@gmail.com',
    description=('interface for ir remote controllers provided with slight-gen minicomp'
                 'operate the desktop using ir remote'),
    license='GPLV3',
    packages=[''],
    test_suite='',
    install_requires=['pyautogui', 'python-lirc'],
    keywords="operate mate-desktop ir-remote-controller",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
