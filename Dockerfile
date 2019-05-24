FROM alpine

RUN apk add --no-cache bind

# Zones
VOLUME "/var/bind"

# Main config
VOLUME "/etc/bind/named.conf"

EXPOSE 53/tcp
EXPOSE 53/udp

ENTRYPOINT [ "/usr/sbin/named", "-f", "-g" ]