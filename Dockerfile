FROM python:2.7-alpine

RUN pip install bottle
RUN pip install boto3

COPY sample-api.py .

CMD [ "python", "./sample-api.py" ]

EXPOSE 8080