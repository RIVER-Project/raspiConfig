#!/bin/bash

if [ ! -d '/home/raspi/bin' ]; then
        sudo mkdir /home/raspi/bin
fi
sudo cp startUpScript.sh /home/raspi/bin/
sudo chmod 777 /home/raspi/bin/startUpScript.sh
sudo cp startUp.service /lib/systemd/system

cd /home/raspi/Desktop

sudo apt update
sudo apt upgrade

sudo apt install neovim

sudo apt-get install avahi-daemon

sudo pip install Flask --break-system-packages
sudo apt install python3-opencv
sudo apt install -y python3-picamera2
sudo pip3 install adafruit-circuitpython-servokit --break-system-packages

sudo apt install git
read -p "Enter git username: " username
git config --global user.name $username
read -p "Enter git email: " email
git config --global user.email $email

git clone https://github.com/mateisorodoc/Rover.git

sudo systemctl daemon-reload
sudo systemctl enable startUp
sudo systemctl start startUp
