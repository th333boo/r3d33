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
USER="th333boo"
SRV_URL="io.th333boo.com"
SRV_DEFAULT="127.0.0.1"
PORT("80","443","3338")
TOOLS("python3","tor","git","pip3","nginx")
PIP_TOOLS("ed25519","python-decouple","scrapy")

printf '\033[32m\nUPDATE OK \033[0m\n'
echo "==============================="
## UPDATER SYSTEM
git clone https://github.com/th333boo/r3dth1rth33n.git $PATH_INSTALL_FOLDER/
git pull $PATH_INSTALL_FOLDER/r3dth1rth33n/
chmod +x $PATH_INSTALL_FOLDER/r3dth1rth33n/installer.sh
sh $PATH_INSTALL_FOLDER/
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok

printf '\033[32m\nBANNER \033[0m\n'
echo "==============================="
## HEADER INTRO
cat $HEADER

printf '\033[32m\nUSER CREATED \033[0m\n'
echo "==============================="
## CREATE USER MACHINE
for str in ${USER[@]};
do useradd ${USER[@]} -m -s /bin/bash -d "/home/${$USER[$str]}/"

printf '\033[32m\nTOOLS INSTALL FINISHED \033[0m\n'
echo "==============================="
## INSTALL TOOLS
apt update
for str in ${TOOLS[@]};do apt install $str -y ; done
for str in ${PIP_TOOLS[@]};do apt install $str -y ; done
pip3 install --pre scapy[complete]

printf '\033[32m\nWEBSERVER INSTALL FINISHED \033[0m\n'
echo "==============================="
## WEBSERVER CONFIG
mkdir -p /var/log/nginx/$SRV_URL
tee /etc/nginx/conf.d/$SRV_URL > /dev/null << EOF
## HTTPS CONFIG
server {
        listen 443 ssl http2;
        listen [::]:443 ssl http2;
        server_name www.$SRV_URL $SRV_URL;

        root /var/www/$SRV_URL/;
        index index.html;

        ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem;
        ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;

        access_log /var/log/nginx/$SRV_URL/access.log;
        error_log /var/log/nginx/$SRV_URL/error.log warn;
}
EOF
tee /etc/nginx/conf.d/$SRV_DEFAULT > /dev/null << EOF
## HTTPS CONFIG
server {
        listen 443 ssl http2;
        listen [::]:443 ssl http2;
        server_name _ ;

        root /var/www/;
        index index.html;

        ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem;
        ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log warn;
}
EOF
printf '\033[32m\nTOR INSTALL FINISHED \033[0m\n'
echo "==============================="
## TOR PROXY INSTALL
apt install tor

printf '\033[32m\nTOR CONFIG FINISHED \033[0m\n'
echo "==============================="
## TOR CONFIG

printf '\033[32m\nSPAM SYSTEM INSTALL FINISHED \033[0m\n'
echo "==============================="
## SPAM SYSTEM
