#!/usr/bin/env bash
#
# install.sh
#
# install the service and the WSGI web app on
# Raspbian Jessie for XmasTrain 2017
#
# by Darren Dunford
#

# script control variables
appdir="/opt/xmastrain"

# update package manager
apt-get update

# install required modules
apt-get install -y python3-pip
pip3 install RPLCD python3-smbus

# create directory structure for app and webapp
mkdir -p $appdir
chgrp -R pi $appdir

# copy webapp and wsgi files
cp xmastrain.py $appdir

# install service file
cp signals.service /lib/systemd/system
chmod 644 /lib/systemd/system/signals.service

# restart Apache and xmastrain service
systemctl daemon-reload
systemctl restart signals
systemctl enable signals