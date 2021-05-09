
FROM python:3.9-alpine3.13

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN mkdir /app
COPY ./app /app
WORKDIR /app

# Creates a non-root user and adds permission to access the /app folder
RUN addgroup -S django \
    && adduser -S -G django django
RUN chown -R django /app
USER django

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "inmuebles.wsgi"]
