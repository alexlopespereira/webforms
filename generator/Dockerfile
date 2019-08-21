FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt && apk add bash
COPY . /code/
CMD bash -c "python3 run_generator.py"