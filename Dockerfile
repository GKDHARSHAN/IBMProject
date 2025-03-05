# Use official Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Copy Prometheus config
COPY prometheus.yml /etc/prometheus/prometheus.yml

# Expose Flask and Prometheus ports
EXPOSE 8000 9090

# Run both Flask and Prometheus
CMD ["sh", "-c", "python app.py & prometheus --config.file=/etc/prometheus/prometheus.yml"]
