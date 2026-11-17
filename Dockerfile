
FROM python:3.11-slim

WORKDIR /app

# Install GeoDjango's required geographical libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project files
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
