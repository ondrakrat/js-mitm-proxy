#!/bin/bash
if [ "$1" -eq "enable" ]
    then
        sudo sysctl -w net.ipv4.ip_forward=1
        sudo iptables -t nat -A PREROUTING -i wlan1 -p tcp --dport 443 -j REDIRECT --to-port 8080
        sudo iptables -t nat -A PREROUTING -i wlan1 -p tcp --dport 80 -j REDIRECT --to-port 8080
elif [ "$1" -eq "disable" ]
    then
        sudo sysctl -w net.ipv4.ip_forward=0
        sudo iptables -t nat -A PREROUTING -i wlan1 -p tcp --dport 443 -j REDIRECT --to-port 8080 -D
        sudo iptables -t nat -A PREROUTING -i wlan1 -p tcp --dport 80 -j REDIRECT --to-port 8080 -D
else
    echo "Usage: ipforwarding.sh enable|disable"
fi
