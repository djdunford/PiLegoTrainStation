#!/usr/bin/env bash
#
# install.sh
#
# install the service to run on startup
#
# by Darren Dunford
#

# script control variables
appdir="/opt/signals"

# update package manager
apt-get update

# install required modules
apt-get install -y python3-pip python3-smbus
pip3 install RPLCD

# create directory structure for app and webapp
mkdir -p $appdir
chgrp -R pi $appdir

# copy webapp and wsgi files
cp onesignal.py $appdir

# install service file
cp signals.service /lib/systemd/system
chmod 644 /lib/systemd/system/signals.service

# restart Apache and signals service
systemctl daemon-reload
systemctl restart signals