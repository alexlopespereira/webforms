FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt && apk add bash
COPY . /app/
CMD bash -c "python3 setup.py && python3 run_generator.py"