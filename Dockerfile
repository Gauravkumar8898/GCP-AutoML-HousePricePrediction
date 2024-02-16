# 1. Base image
FROM python:3.8

# 2. Specify directory where all subsequent instructions are run
WORKDIR /root

# 3. Copy files
COPY src /root/src
COPY src/utils /root/src/utils
COPY src/pipeline /root/src/pipeline
COPY requirements.txt /root/requirements.txt

# 4. Install dependencies
RUN pip install -r /root/requirements.txt

