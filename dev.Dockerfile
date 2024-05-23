FROM python:alpine3.11

COPY . /app/

WORKDIR /app

RUN apk update && apk upgrade
RUN apk add --no-cache build-base
RUN apk add --no-cache g++ jpeg-dev zlib-dev libjpeg make gcc
RUN apk add --no-cache libffi-dev
RUN apk add --no-cache python3-dev  py-pip
RUN apk add --no-cache py-pip py-virtualenv
RUN pip install --upgrade pip setuptools
RUN pip install --upgrade pip
RUN pip install wheel
RUN make install

EXPOSE 5000



ENV NEW_RELIC_APP_NAME="codesquad-blacklist-api"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LICENSE_KEY=2faaaccf69bd3678382e3db100ed02b3FFFFNRAL
ENV NEW_RELIC_LOG_LEVEL=info

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:application"]

ENTRYPOINT ["newrelic-admin", "run-program"]