# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to /app
COPY . .

# Expose port 8000, as required by Azure App Service
EXPOSE 8000

# Command to run the Streamlit app, configured to use port 8000
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]
