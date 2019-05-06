FROM homecentral/base:feature-poc

ADD entrypoint.sh /entrypoint.sh
ADD init.py /init.py
ADD *.j2 /
ADD config-schema.json /config-schema.json

RUN apk add --no-cache bind && \
    chmod +x /entrypoint.sh

ENTRYPOINT [ "/bin/ash", "/entrypoint.sh" ]