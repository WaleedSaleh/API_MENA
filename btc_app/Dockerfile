FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps
COPY . /app/