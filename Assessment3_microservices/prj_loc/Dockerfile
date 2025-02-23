FROM python:3.10-slim

# Install MySQL development libraries and pkg-config
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# installs this into container from central docker repo
WORKDIR /app    
# this will create a app folder in our container
COPY req.txt .
#copy this current folder into the workdir
RUN pip3 install -r req.txt

COPY . .
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
