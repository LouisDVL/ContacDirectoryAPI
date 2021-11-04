FROM python:alpine

ENV PYTHONUNBUFFERED=1
RUN apk add --virtual build-deps gcc musl-dev && apk add postgresql-dev

WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]