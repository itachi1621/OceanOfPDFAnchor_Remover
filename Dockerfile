# Use Python 3.11 as base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all the necessary files to the container
COPY . .

# Create the input and output directories inside the container
RUN mkdir -p /app/input /app/output && chmod -R 777 /app/input /app/output

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python", "OceanOfPDFAnchor_Remover.py"]

