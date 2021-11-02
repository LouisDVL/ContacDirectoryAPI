FROM python:3

ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get -y install nodejs
RUN apt-get update && apt-get -y install npm

WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
RUN cd client && npm install && npm run build