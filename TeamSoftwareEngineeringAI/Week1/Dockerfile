# Use a base Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (optional, useful for Jupyter extensions)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    jupyterlab \
    flask

# Expose Flask (5000) and JupyterLab (8888) default ports
EXPOSE 5000 8888

# Set environment variables for JupyterLab
ENV JUPYTER_ALLOW_INSECURE_WRITES=true

# Add an alias for starting JupyterLab
RUN echo "alias START_JUPYTER='jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root'" >> /root/.bashrc

# Default command will keep the container ready for interactive sessions
CMD ["bash"]
