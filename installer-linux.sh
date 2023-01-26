#!/bin/bash
HEADER="
### ### ### ### ### ### ### ### ###
###         th333boo            ###
### telegram: @th333boo         ###
### www: https://th333boo.com   ###
### mail: contact@th333boo.com  ###
###     all right reserved      ###
### ### ### ### ### ### ### ### ###"

PATH_INSTALL_FOLDER='/opt'
declare -a USER=("noc" "th333boo")
declare -a SRV_URL=("***.ngrok.io" "io.th333boo.com")
declare -a PORT("80" "443" "3338")
declare -a TOOLS("python3" "tor" "git")

## UPDATER SCRIPT SYSTEM
git clone https://github.com/th333boo/r3dth1rth33n.git $PATH_INSTALL_FOLDER/
git pull $PATH_INSTALL_FOLDER/r3dth1rth33n/
chmod +x $PATH_INSTALL_FOLDER/r3dth1rth33n/installer-linux.sh | sh

printf '\033[32m\nUPDATE OK \033[0m\n'
echo "==============================="

## HEADER INTRO
cat $HEADER

printf '\033[32m\nBANNER \033[0m\n'
echo "==============================="

## CREATE USER MACHINE
for str in ${USER[@]};
do useradd ${USER[@]} -m -s /bin/bash -d "/home/${$USER[$str]}/"

printf '\033[32m\nUSER CREATED \033[0m\n'
echo "==============================="

## INSTALL TOOLS
apt install $TOOLS

printf '\033[32m\nTOOLS INSTALL FINISHED \033[0m\n'
echo "==============================="
## WEBSERVER CONFIG

## TOR PROXY INSTALL

## TOR CONFIG

## SPAM SYSTEM
