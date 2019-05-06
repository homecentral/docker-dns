#!/usr/bin/env bash

ls /

python3 init.py

# ls /etc/bind/*.zone

# cat /etc/bind/example.com.zone

/usr/sbin/named -f -g -4 -d 1