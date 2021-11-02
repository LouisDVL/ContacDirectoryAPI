FROM python:alpine

ENV PYTHONUNBUFFERED=1
RUN apk update && apk add --update npm
RUN apk add --virtual build-deps gcc musl-dev && apk add postgresql-dev
RUN addgroup app && adduser -S -G app app
USER app

WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
USER root
RUN cd client && npm install && npm run build
USER app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]