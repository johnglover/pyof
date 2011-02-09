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
from distutils import sysconfig 
import sys

def get_platform():
    """Return the current platform if supported, or 'unsupported' if not."""
    if sys.platform[:6] == "darwin":
        return "darwin"
    else:
        return "unsupported"

# check that the current platform is supported
if get_platform() == "unsupported":
    print "Error: Cannot currently build on this platform. "
    print "       Only Mac OS X is supported."
    exit(1)

# include directories
includes = """../libs/fmodex/include/ 
              ../libs/FreeImage/include/ 
              ../libs/freetype/include/ 
              ../libs/freetype/include/freetype2/
              ../libs/glee/include/ 
              ../libs/poco/include/ 
              ../libs/rtAudio/include/
              ../libs/openFrameworks/app/ 
              ../libs/openFrameworks/communication/
              ../libs/openFrameworks/events/ 
              ../libs/openFrameworks/graphics/
              ../libs/openFrameworks/sound/ 
              ../libs/openFrameworks/utils/
              ../libs/openFrameworks/video/ 
              ../libs/openFrameworks/""".split()

# source files
source_files = """openframeworks/openframeworks.i
                  ../libs/openFrameworks/app/ofAppGlutWindow.cpp 
                  ../libs/openFrameworks/app/ofAppRunner.cpp
                  ../libs/openFrameworks/communication/ofArduino.cpp 
                  ../libs/openFrameworks/communication/ofSerial.cpp
                  ../libs/openFrameworks/graphics/ofBitmapFont.cpp 
                  ../libs/openFrameworks/graphics/ofGraphics.cpp
                  ../libs/openFrameworks/graphics/ofImage.cpp 
                  ../libs/openFrameworks/graphics/ofTexture.cpp
                  ../libs/openFrameworks/graphics/ofTrueTypeFont.cpp
                  ../libs/openFrameworks/sound/ofSoundPlayer.cpp 
                  ../libs/openFrameworks/sound/ofSoundStream.cpp
                  ../libs/openFrameworks/utils/ofMath.cpp 
                  ../libs/openFrameworks/utils/ofUtils.cpp
                  ../libs/openFrameworks/video/ofQtUtils.cpp 
                  ../libs/openFrameworks/video/ofVideoGrabber.cpp
                  ../libs/openFrameworks/video/ofVideoPlayer.cpp""".split()

# addons
# addon_source_files = """../addons/ofxThread/src/ofxThread.cpp""".split()
# source_files.extend(addon_source_files)

# set library directories and add frameworks for OS X
if get_platform() == "darwin":
    includes.extend("""/System/Library/Frameworks/OpenGL.framework/Headers
                       /System/Library/Frameworks/GLUT.framework/Headers
                       /System/Library/Frameworks/AGL.framework/Headers
                       /System/Library/Frameworks/ApplicationServices.framework/Headers
                       /System/Library/Frameworks/AudioToolbox.framework/Headers
                       /System/Library/Frameworks/Carbon.framework/Headers
                       /System/Library/Frameworks/CoreAudio.framework/Headers
                       /System/Library/Frameworks/CoreFoundation.framework/Headers
                       /System/Library/Frameworks/CoreServices.framework/Headers
                       /System/Library/Frameworks/Quicktime.framework/Headers""".split())
    link_args = """-framework OpenGL
                   -framework GLUT
                   -framework AGL
                   -framework ApplicationServices
                   -framework AudioToolbox
                   -framework Carbon
                   -framework CoreAudio
                   -framework CoreFoundation
                   -framework CoreServices
                   -framework Quicktime
                   ../libs/FreeImage/lib/osx/freeimage.a 
                   ../libs/freetype/lib/osx/freetype.a 
                   ../libs/glee/lib/osx/GLee.a 
                   ../libs/rtAudio/lib/osx/rtAudio.a 
                   ../libs/fmodex/lib/osx/libfmodex.dylib
                   ../libs/poco/lib/osx/CppUnit.a
                   ../libs/poco/lib/osx/PocoFoundation.a
                   ../libs/poco/lib/osx/PocoNet.a 
                   ../libs/poco/lib/osx/PocoUtil.a 
                   ../libs/poco/lib/osx/PocoXML.a""".split()
    # Remove any 64-bit flags from distutils sysconfig config_vars, the Quicktime
    # framework is 32-bit only.
    # There doesn't seem to be a nicer way to change these values.
    config_vars = sysconfig.get_config_vars()
    config_vars['PY_CFLAGS'] = config_vars['PY_CFLAGS'].replace("-arch x86_64 ", "") 
    config_vars['CFLAGS'] = config_vars['CFLAGS'].replace("-arch x86_64 ", "") 
    config_vars['BLDSHARED'] = config_vars['BLDSHARED'].replace("-arch x86_64 ", "") 
    config_vars['LDFLAGS'] = config_vars['LDFLAGS'].replace("-arch x86_64 ", "") 
    config_vars['LDSHARED'] = config_vars['LDSHARED'].replace("-arch x86_64 ", "") 

# Build the extension
doc_lines = __doc__.split("\n")
openframeworks = Extension("openframeworks/_openframeworks", 
                           sources = source_files,
                           include_dirs = includes,
                           extra_link_args = link_args,
                           swig_opts = ['-c++']) 

# install setup data_files in the same folder as the module
# from distutils.command.install import INSTALL_SCHEMES 
# for scheme in INSTALL_SCHEMES.values(): 
    # scheme['data'] = scheme['platlib'] 

setup(name='openframeworks',
      description = doc_lines[0],
      long_description = "\n".join(doc_lines[2:]),
      url = 'http://github.com/johnglover/ofpy',
      download_url = 'http://github.com/johnglover/ofpy',
      license = 'MIT',
      author = 'John Glover',
      author_email = 'john.c.glover@nuim.ie',
      platforms = ["Mac OS-X"],
      version = '006.2',
      ext_modules = [openframeworks],
      packages = ['openframeworks'])
