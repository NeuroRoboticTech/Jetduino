## **Jetduino: The Jetson Embedded Supercomputer Meets Grove Sensors**

Jetduino is an open source platform for connecting Grove Sensors to the Jetson TK1 supercomputers.  Create your own intelligent robot or inventions without the need for soldering!

We brought Grove and the Jetson in a simple and affordable way. Grove sensors allow you to interact and monitor the world. The Jetson lets you store and process data in way that has never been possible for before for embedded systems. Its 192 CUDA cores makes it possible to perform onboard visual proceesing, deep neural network (DNN) control systems, or biologically realistic neural nets for intelligent and adaptive robots. The Jetduino brings both Grove Sensors and the popular Jetson TK1 together in a simple, elegant, and open source design. 

Another awesome feature of the Jetduino is that it also combines the Arduino Microcontroller and the DynamixShield. This allows you to attach an Arduino Due directly into the DynamixShield section of the Jetduino. The DynamixShield is a shield of for the Arduino Due that level shifts all of its signals, and provides Grove ports for the Due. It also has a controller for interfacing with Dynamixel AX/MX smart servos. This makes it very easy to setup the Jetson to do the number crunching for the "Brains" of your robot, while allowing the Due to handle the low level sensor and motor interactions, while communictating with the Jetson.

### How Does it Work?
The Jetduino board is the same size as the Jetson and it is mounted above or below it. Because the Jetson TK1 uses a female 2mm connector on its board, an interface connector was required. This connector ships with the Jetduino. It plugs into the Jetson and a normal Raspberry Pi GPIO ribbon cable is used to connect the Jetduino to the Jetson. Next, connect your Grove sensor. Upload your program. Begin taking in the worlds data!

Most of the Grove interface scripts found in the Jetduino library are modified versions of GrovePi code. GrovePi is a Grove board used for the Raspberry Pi. There are only minor modifications required to use those scripts and libraries on the Jetson. If there is a Grove module you would like to use that is not yet in the Jetduino library you will probably be able to find it in the GrovePi library and modify it. You can find the GrovePi library here: [https://github.com/DexterInd/GrovePi](https://github.com/DexterInd/GrovePi)

### Jetson Compatibility
The Jetduino is compatible with the Jetson TK1 and the Arduino Due. If there is enough demand for this, then it is possible new versions for the Jetson TX1 and Geniuno 101 could be built.

### Getting Started
Getting started is easy. Check out our Getting Started With Jetduino Guide [here](http://www.NeuroRoboticTech.com/Projects/Jetduino/get-started-with-the-Jetduino/). 
We have an extensive library that covers most Grove sensors. You can find it on the Github repo.  You won’t need to hack much at all with our library: get started coding in Python and C now! 

### Want to use a sensor not in the library yet?  
Ask us in the [forums](http://neurorobotictech.com/Community/Forum). Want to use the Jetduino in a language not currently supported? [Ask and we will help](http://neurorobotictech.com/Community/Forum).

### Programming the Jetduino
The Jetduino can be programmed in Python, C, and C++ on the Jetson.  Simply start with one of our [example projects](http://www.NeuroRoboticTech.com/Projects/Jetduino/projects-for-the-Jetson/) or [example code](https://github.com/NeuroRoboticTech/Jetduino).  

### Getting Help
Need help? We [have a forum here where you can ask questions or make suggestions](http://neurorobotictech.com/Community/Forum).

### Getting Into It
Want to hack it open or make your own from scratch? With full hardware and software designs, you can remix and duplicate to your hearts content.

See more at the [Jetduino Site](http://NeuroRoboticTech.com/Projects/Jetduino/)

## License

The MIT License (MIT)

Jetduino for the Jetson TK1/TX1: an open source platform for connecting 
Grove Sensors to the Jetson embedded supercomputers.
Copyright (C) 2016  NeuroRobotic Technologies, LLC

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
