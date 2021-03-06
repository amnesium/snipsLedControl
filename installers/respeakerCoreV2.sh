#!/usr/bin/env bash

echo "############### Respeaker Core V2 installation ########################"
echo "############## Please run this script with sudo #######################"

pip uninstall -y gpiozero
pip uninstall -y RPi.GPIO

apt-get install -y python-mraa

sed -i -e "s/WorkingDirectory=\/home\/pi\//WorkingDirectory=\/home\/"$(logname)"\//" /etc/systemd/system/snipsledcontrol.service

echo "############################## All done! ##############################"
echo "################################ Enjoy! ###############################"