#!/usr/bin/env bash

echo "############### Respeaker Mic Array V1 installation ########################"
echo "################ Please run this script with sudo ##########################"

USER=$(logname)

apt-get install libusb-1.0-0-dev
pip install click
pip install pyusb

cd /home/$USER
rm -rf /home/$USER/mic_array_dfu
git clone https://github.com/respeaker/mic_array_dfu.git
cd mic_array_dfu
make
./dfu --download respeaker_mic_array_8ch_raw.bin

echo "############################## All done! ##############################"