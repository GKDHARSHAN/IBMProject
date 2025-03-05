# Use official Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 80

# Run the application
CMD ["python", "app.py"]
