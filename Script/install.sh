#! /bin/bash
echo "Welcome to Jetduino Installer."
echo " "
echo "Requirements:"
echo "1) Must be connected to the internet"
echo "2) This script must be run as root user"
echo " "
echo "Steps:"
echo "1) Installs package dependencies:"
echo "   - python-pip         alternative Python package installer"
echo "   - git                fast, scalable, distributed revision control system"
echo "   - libi2c-dev         userspace I2C programming library development files"
echo "   - python-serial      pyserial - module encapsulating access for the serial port"
echo "   - i2c-tools          This Python module allows SMBus access through the I2C /dev"
echo "   - python-sysfs-gpio  Python tools for gpio access"
echo "   - python-smbus       Python bindings for Linux SMBus access through i2c-dev"
echo "   - minicom            friendly menu driven serial communication program"
echo " "
echo "Special thanks to Joe Sanford at Tufts University. This script was derived from his work. Thank you Joe!"
#echo " "
#echo "Jetson wil reboot after completion."
echo " "
echo -e "Press \E[32mENTER\E[0m to begin... or \E[91mctrl+c\E[0m to abort"
# read
sleep 5

echo " "
echo "Check for internet connectivity..."
echo "=================================="
wget -q --tries=2 --timeout=100 http://google.com
if [ $? -eq 0 ];then
	echo "Connected"
else
	echo "Unable to Connect, try again !!!"
	exit 0
fi

echo " "
echo "Installing Dependencies"
echo "======================="
sudo apt-get install python-pip git libi2c-dev python-serial i2c-tools python-smbus arduino minicom python-dev

git clone https://github.com/derekstavis/python-sysfs-gpio.git
cd python-sysfs-gpio
python setup.py install
cd ..
echo "Dependencies Installed"

echo " "
echo "Install smbus for python"
sudo apt-get install python-smbus

echo "Install jetduino Python for global use "
echo "============================="
cd ../Software/Python
python setup.py install

echo " "
echo "Jetduino install is complete."
echo "You still need to install the Firmware sketch to the Arduino Due."
echo "Then you can begin using the Jetduino! "

#echo " "
#echo "Please restart to implement changes!"
#echo "  _____  ______  _____ _______       _____ _______ "
#echo " |  __ \|  ____|/ ____|__   __|/\   |  __ \__   __|"
#echo " | |__) | |__  | (___    | |  /  \  | |__) | | |   "
#echo " |  _  /|  __|  \___ \   | | / /\ \ |  _  /  | |   "
#echo " | | \ \| |____ ____) |  | |/ ____ \| | \ \  | |   "
#echo " |_|  \_\______|_____/   |_/_/    \_\_|  \_\ |_|   "
#echo " "
#echo "Please restart to implement changes!"
#echo "To Restart type sudo reboot"

#echo "To finish changes, we will reboot the Jetson."
#echo "Pi must reboot for changes and updates to take effect."
#echo "If you need to abort the reboot, press Ctrl+C.  Otherwise, reboot!"
#echo "Rebooting in 5 seconds!"
#sleep 1
#echo "Rebooting in 4 seconds!"
#sleep 1
#echo "Rebooting in 3 seconds!"
#sleep 1
#echo "Rebooting in 2 seconds!"
#sleep 1
#echo "Rebooting in 1 seconds!"
#sleep 1
#echo "Rebooting now!  Your Jetduino wake up with a freshly updated Jetson!"
#sleep 1
#sudo reboot
