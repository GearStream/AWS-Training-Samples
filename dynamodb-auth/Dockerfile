FROM python:2-onbuild

RUN mkdir ~/.aws
ADD aws_config ~/.aws/config

CMD [ "python", "/usr/src/app/service.py" ] 