FROM python:3.11-slim-bullseye

WORKDIR /app

# Copy and install dependencies
COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

RUN mkdir -p /config

# Copy the raw source code
COPY . .

# Unfolded Circle Environment Variables
ENV UC_DISABLE_MDNS_PUBLISH="false"
ENV UC_MDNS_LOCAL_HOSTNAME=""
ENV UC_INTEGRATION_INTERFACE="0.0.0.0"
ENV UC_INTEGRATION_HTTP_PORT="9090"
ENV UC_CONFIG_HOME="/config"
ENV PYTHONPATH=/app

# Container Metadata
LABEL org.opencontainers.image.source=https://github.com/joemacjr92/ucr-integration-sonyADCP
LABEL org.opencontainers.image.description="Sony ADCP integration for Unfolded Circle Remote"
LABEL org.opencontainers.image.licenses=MPL-2.0

# Run the raw Python script instead of a compiled binary
CMD ["python3", "-u", "driver.py"]