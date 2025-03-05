# Use official Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies (including Prometheus client)
RUN pip install -r requirements.txt && pip install prometheus_client

# Copy Prometheus configuration
COPY prometheus.yml /etc/prometheus/prometheus.yml

# Expose the application port and Prometheus metrics port
EXPOSE 80 8000

# Run the application
CMD ["python", "app.py"]
