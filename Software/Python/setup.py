#!/usr/bin/python #!/usr/bin/env python
#
# Jetduino Python Setup
#
# The Jetduino connects the Jetson and Grove sensors.  You can learn more about the Jetduino here:  http://www.NeuroRoboticTech.com/Projects/Jetduino
#
# Have a question about this example?  Ask on the forums here:  http://www.NeuroRoboticTech.com/Forum
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Jetduino for the Jetson TK1/TX1: an open source platform for connecting 
Grove Sensors to the Jetson embedded supercomputers.
Copyright (C) 2016  NeuroRobotic Technologies

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
# To install the Jetduino library systemwide, use: sudo python setup.py install

import setuptools

__name__         = 'jetduino'
__description__  = 'Drivers and examples for using the Jetduino in Python'
__author__       = 'David Cofer'
__version__      = '1.0.0'
__author_email__ = 'dcofer@NeuroRoboticTech.com'
__author_site__  = 'http://www.NeuroRoboticTech.com/Projects/Jetduino/'

requirements = ['sysfs-gpio']

setuptools.setup(
    name                 = __name__,
    description          = __description__,
    version              = __version__,
    author               = __author__,
    author_email         = __author_email__,
    url                  = __author_site__,
	py_modules=['jetduino', 'jetduino_pins'],

    install_requires     = requirements,
    include_package_data = True,

    packages = setuptools.find_packages(),  # include all packages under src
)
