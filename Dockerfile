# Use an official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all the necessary files to the container
COPY . .

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python", "OceanOfPDFAnchor_Remover.py"]

