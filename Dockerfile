FROM scratch

ARG DRIVER_ID

COPY . /driver/

WORKDIR /driver

ENTRYPOINT ["/driver/driver"]