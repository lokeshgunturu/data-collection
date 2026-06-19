# Use lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy your Python file into container
COPY . .

# Run your script (change filename if needed)
CMD ["/bin/bash"]
