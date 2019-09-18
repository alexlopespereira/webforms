# FROM tiangolo/meinheld-gunicorn:python3.7-alpine3.8
# LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"
# RUN pip install flask
# COPY ./app /app
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install -r requirements.txt

FROM tiangolo/uwsgi-nginx:python3.6-alpine3.8

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install flask

# Port to be used
ENV LISTEN_PORT 8088
EXPOSE 8088

# URL under which static (not modified by Python) files will be requested
# They will be served by Nginx directly, without being handled by uWSGI
ENV STATIC_URL /static
# Absolute path in where the static files wil be
ENV STATIC_PATH /app/static

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
# ENV STATIC_INDEX 1
ENV STATIC_INDEX 1

# Add demo app
COPY ./app /app
WORKDIR /app

# Install Requirements
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Make /app/* available to be imported by Python globally to better support several use cases like Alembic migrations.
ENV PYTHONPATH=/app

# Move the base entrypoint to reuse it
RUN mv /entrypoint.sh /uwsgi-nginx-entrypoint.sh
# Copy the entrypoint that will generate Nginx additional configs
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Run the start script provided by the parent image tiangolo/uwsgi-nginx.
# It will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
CMD ["/start.sh"]