FROM scratch

ARG DRIVER_ID

COPY artifacts/bin/ /driver/
COPY artifacts/driver.json /driver/driver.json

WORKDIR /driver

ENTRYPOINT ["/driver/driver"]