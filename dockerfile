FROM python:3.12-slim

ARG secret_key
ARG sentry_url

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . .

RUN python manage.py collectstatic

COPY .env .env

RUN export $(grep -v '^#' .env | xargs)

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



RUN echo "SECRET_KEY=$secret_key" > /app/oc_lettings_site/.env
RUN echo "DSN=$sentry_url" >> /app/oc_lettings_site/.env