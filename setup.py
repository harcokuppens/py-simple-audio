# Simpleaudio Python Extension
# Copyright (C) 2015, Joe Hamilton, 2024, Harco Kuppens
# MIT License (see LICENSE.txt)

# see: https://setuptools.pypa.io/en/latest/userguide/ext_modules.html
from setuptools import setup, Extension
import sys
from os import path

platform_sources = []
platform_libs = []
platform_link_args = []
platform_compile_args = []

if sys.platform == 'darwin':
    platform_sources = ['c_src/simpleaudio_mac.c', 'c_src/posix_mutex.c']
    platform_link_args = ['-framework', 'AudioToolbox']
    platform_compile_args = ['-mmacosx-version-min=10.6']
elif sys.platform.startswith("linux"):
    platform_sources = ['c_src/simpleaudio_alsa.c', 'c_src/posix_mutex.c']
    platform_libs = ['asound']
elif sys.platform == 'win32':
    platform_sources = ['c_src/simpleaudio_win.c', 'c_src/windows_mutex.c']
    platform_libs = ['Winmm', 'User32']
else:
    pass
    # define a compiler macro for unsupported ?

simpleaudio_c_ext = Extension(
    name='simpleaudio._simpleaudio',
    sources=platform_sources + ['c_src/simpleaudio.c'],
    libraries=platform_libs,
    extra_compile_args=platform_compile_args,
    extra_link_args=platform_link_args,
    define_macros=[('DEBUG', '0')])


setup( ext_modules=[simpleaudio_c_ext] )
