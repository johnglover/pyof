pyof: Python bindings for openFrameworks
========================================

Currently these bindings are for Mac OS X only. They only wrap the
core openFrameworks library (don't include any of the addons).


About OpenFrameworks
--------------------

OpenFrameworks is a C++ library designed to assist the creative process by 
providing a simple and intuitive framework for experimentation.

The library is designed to work as a general purpose glue, and wraps together 
several commonly used libraries under a tidy interface: OpenGL for graphics, 
rtAudio for audio input and output, freeType for fonts, freeImage for image 
input and output, Quicktime for video playing and sequence grabbing.

For more information see [http://www.openframeworks.cc](http://www.openframeworks.cc).


Dependencies
------------

* [openFrameworks 0062](http://www.openframeworks.cc)
* [Python](http://www.python.org) - tested with 2.6.5
* [SWIG](http://http://www.swig.org/) - tested with version 2.0.1


Installation
------------

Copy the pyof folder to your openFrameworks root folder. The location is important,
as the openFrameworks libraries are linked using relative path names. The directory
structure should look like this:

    openFrameworks
    |
    --- addons
    |
    --- apps
    |
    --- libs
    |
    --- other
    |
    --- pyof
    |
    --- scripts
    |
    --- xcode templates

In the pyof folder, run the following command to build the extension module:

    $ python setup.py build

Then to install the module in your Python site-packages directory:

    $ python setup.py install

Finally, if you do not have a copy of the fmodex dynamic library in your
/usr/local/lib folder (or equivalent), run the following command:

    sudo cp ../libs/fmodex/lib/osx/libfmodex.dylib /usr/local/lib


### A note for Snow Leopard Users

As the Quicktime framework is 32-bit only, you must use a version of Python
that supports 32-bit. The version is provided by Apple and that comes with 
Snow Leopard is compiled for PPC, i386 and x86_64 architectures. If you
build your own version of Python, make sure that the i386 architecture
is included at least. 

The following commands will build and install Python 
for i386 and x86_64 (Intel processors) on Snow Leopard:

    ./configure --enable-framework 
                --enable-universalsdk=/Developer/SDKs/MacOSX10.6.sdk 
                --with-universal-archs=intel

    make

    sudo make frameworkinstall


Use
---

Have a look at the file sinewave.py in the examples folder.


Contributing
------------

Send any comments, queries, suggestions or bug reports to j at johnglover dot net.
