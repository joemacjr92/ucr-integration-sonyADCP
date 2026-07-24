FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY src/ ./src/
COPY driver.json .
# Copies the icon file if it exists
COPY *.png ./ 

# The Sony ADCP integration defaults to 8090, but check your driver.json
ENV UC_INTEGRATION_HTTP_PORT=8090
EXPOSE 8090

# Execute the main driver loop
CMD ["python3", "src/driver.py"]
