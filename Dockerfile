FROM python:3.11-slim

WORKDIR /app

# Copy dependency list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all python files, driver.json, and the icon
COPY *.py .
COPY driver.json .
COPY *.png ./ 

# Set the port
ENV UC_INTEGRATION_HTTP_PORT=8090
EXPOSE 8090

# We need to run the main python file. 
# NOTE: Check if your main file is named something other than 'main.py' 
# (e.g., 'sony_adcp.py' or 'integration.py') and change the line below if necessary.
CMD ["python3", "main.py"]
