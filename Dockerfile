FROM python:3.7.0

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        mysql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
#COPY ./api /usr/src/app
#COPY ./manage.py /usr/src/app
#COPY ./requirements.txt /usr/src/app
COPY ./ /usr/src/app/
EXPOSE 8000
RUN pip install -r requirements.txt
RUN pip install django-request-logging
CMD ["/usr/src/app/migrate_run.sh","db"]
