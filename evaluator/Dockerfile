FROM gcc:9.4.0

RUN apt-get update && \
    apt-get install -y python3 && \
    apt install -y python3-pip

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade setuptools && \
    python3 -m pip install flask flask-cors requests

COPY . /app

EXPOSE 5000

CMD ["python3", "api.py"]