FROM python:3.9.1-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY .env .env

RUN pip install -r requirements.txt

COPY wsgi.py wsgi.py
COPY core ./core

RUN flask init-db
RUN flask create-users

EXPOSE 5000
CMD ["python", "wsgi.py"]