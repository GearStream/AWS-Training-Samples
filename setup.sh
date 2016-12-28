#!/bin/sh
sudo yum update -y
sudo yum install -y docker
sudo service docker start

sudo yum install -y git

git clone https://github.com/GearStream/AWS-Training-Samples.git

sudo docker build -t gearstream/simple-service AWS-Training-Samples/dynamodb-auth
sudo docker run -d -p 8080:8080 gearstream/simple-service
