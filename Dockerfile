FROM python:3.8
RUN pip install --upgrade pip
COPY src app/src
COPY requirements.txt requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ADD main.py .
CMD ["python", "main.py"]
