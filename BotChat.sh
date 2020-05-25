#!/bin/bash
clear
figlet BOTCHAT | lolcat
echo '~# TEAM : KEBUMEN GREY HAT TEAM'
echo
while [ true ]
do
   read -p "You: " p;
   echo "Bot: "$(shuf -n1 list)
done
