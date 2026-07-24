FROM python:3.11-slim

WORKDIR /app

# Copy dependency list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the core python folder
COPY intg-sonyadcp/ ./intg-sonyadcp/
COPY driver.json .
COPY *.png ./ 

# Set the port
ENV UC_INTEGRATION_HTTP_PORT=8090
EXPOSE 8090

# We need to run the main python file inside the folder. 
# NOTE: Check if your main file is named something other than 'main.py' 
# (e.g., 'sony_adcp.py' or 'driver.py') and change the line below if necessary.
CMD ["python3", "intg-sonyadcp/main.py"]
