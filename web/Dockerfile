#FROM alpin_wdp_image:latest
#FROM python:3.7-stretch
FROM stretch_wdp_image:1.0

COPY .msmtprc /root
COPY .mailrc /root

RUN rm /usr/local/lib/python3.7/site-packages/crontab.py

COPY crontab.py /usr/local/lib/python3.7/site-packages 
COPY . /

USER root
#RUN rm -rf /var/cache/* && \
#  mkdir /var/cache/apk
RUN pip install --no-index --find-links dependencies xlsx2html packaging
#RUN rm -rf /var/cache/apk/* && \
#  rm -rf /tmp/*

#RUN apk update
#RUN cat manage.py
#apk --update add --no-cache
#RUN apk add gcc \
#  python2-dev \
#  musl-dev \
#  libffi libffi-dev \
#  postgresql-dev \
#  make \
#  nano \
#  curl 


#RUN apt-get update 
#RUN apt-get install -y cron msmtp 
RUN mkdir /var/log/cronlogs

#RUN tar -zxf dependencies.tar.gz && pip install -r requirements.txt --no-index --find-links dependencies
#RUN pip install -r requirements.txt --no-index --find-links dependencies
#RUN pip install -r requirements.txt 

#RUN tar -zxf dependencies.tar.gz
#RUN cd dependencies
#RUN pip install * -f ./ --no-index

RUN chmod +x runserver.sh

ENTRYPOINT ["/runserver.sh"]