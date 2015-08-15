#from distutils.core import setup, Extension
from setuptools import setup, Extension
import sys

platform_sources = []
platform_libs = []
platform_link_args = []
platform_inc_dirs = []

if sys.platform == 'darwin':
    platform_sources = ['simpleaudio_mac.c', 'posix_mutex.c']
    platform_link_args = ['-framework', 'AudioToolbox']
elif sys.platform == 'linux':
    platform_sources = ['simpleaudio_alsa.c', 'posix_mutex.c']
    platform_libs = ['asound']
else:
    pass
    # define a compiler macro for unsupported ?

_simpleaudio_module = Extension(
    '_simpleaudio', 
    sources=platform_sources+['simpleaudio.c'],
    libraries=platform_libs,
    extra_link_args=platform_link_args,
    include_dirs=platform_inc_dirs,
    define_macros = [('DEBUG', '1')])

setup(name = 'simpleaudio',
    version = '1.0',
    description = """The simpleaudio package contains the simpleaudio module 
                     which makes playing wave files in Python very simple.""",
    test_suite="tests",
    py_modules = ["simpleaudio.shiny"],
    ext_modules = [_simpleaudio_module])