FROM python:3.8.7-alpine3.12

COPY . /app
WORKDIR /app

RUN apk add --no-cache --virtual \
    build-dependencies \
    py-pip \
    build-base \
    linux-headers \
    && pip install --editable . \
    && apk del \
    build-dependencies \
    linux-headers

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["GL-DevOps-ProCamp-Entry-Task-Metrics"]
CMD ["--help"]
