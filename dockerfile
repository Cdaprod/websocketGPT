# Use the official Python image as the base
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the WebSocket server script into the container
COPY ws_server.py .

# Set the environment variable
ARG API_KEY
ENV API_KEY=\${API_KEY}

# Expose the WebSocket server port
EXPOSE 8000

# Run the WebSocket server
CMD ["python", "ws_server.py"]
