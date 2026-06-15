FROM scratch

ARG DRIVER_ID

COPY driver /driver/driver
COPY driver.json /driver/driver.json

WORKDIR /driver

ENTRYPOINT ["/driver/driver"]