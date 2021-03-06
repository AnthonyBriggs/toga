#/usr/bin/env python
import io
from setuptools import setup


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='toga',
    version='0.2.0',
    description='A Python native, OS native GUI toolkit.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://pybee.org/toga',
    extras_require={
        # Automatically installed platform backends
        ':sys_platform=="win32"': ['toga-win32'],
        ':sys_platform=="linux"': ['toga-gtk'],
        ':sys_platform=="linux2"': ['toga-gtk'],
        ':sys_platform=="darwin"': ['toga-cocoa'],

        # # Manually requested platform backends
        # 'cocoa': ['toga-cocoa'],
        # 'macos': ['toga-cocoa'],
        # 'gtk': ['toga-gtk'],
        # 'linux': ['toga-gtk'],
        # 'win32': ['toga-win32'],
        # 'ios': ['toga-iOS'],
        # 'android': ['toga-android'],
        # 'django': ['toga-django'],
        # # 'qt': ['toga-qt'],
    },
    license='New BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Widget Sets',
    ],
)
