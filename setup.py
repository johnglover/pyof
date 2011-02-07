#!/usr/bin/env python
"""
pyof: Python bindings for openFrameworks

Openframeworks is a C++ library designed to assist the creative process by 
providing a simple and intuitive framework for experimentation.

The library is designed to work as a general purpose glue, and wraps together 
several commonly used libraries under a tidy interface: openGL for graphics, 
rtAudio for audio input and output, freeType for fonts,freeImage for image 
input and output, quicktime for video playing and sequence grabbing.

For more information see http://www.openframeworks.cc.
"""
from distutils.core import setup, Extension
import sys

def get_platform():
    """Return the current platform if supported, or 'unsupported' if not."""
    if sys.platform[:5] == "linux":
        return "linux"
    elif sys.platform[:6] == "darwin":
        return "darwin"
    else:
        return "unsupported"

def get_version():
    return sys.version[:3]

# check that the current platform is supported
if get_platform() == "unsupported":
    print "Error: Cannot build on this platform. "
    print "       Only Linux, Mac OS X and Windows are currently supported."
    exit(1)

doc_lines = __doc__.split("\n")

setup(name='openframeworks',
      description=doc_lines[0],
      long_description="\n".join(doc_lines[2:]),
      url='http://github.com/johnglover/ofpy',
      download_url='http://github.com/johnglover/ofpy',
      license='MIT',
      author='John Glover',
      author_email='john.c.glover@nuim.ie',
      platforms=["Linux", "Mac OS-X"],
      version='006.2',
      # ext_modules=[openframeworks],
      packages=[])
