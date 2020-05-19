#!/bin/bash
sudo docker rm -f $(sudo docker ps -a -q)
sudo docker-compose build web
sudo docker-compose up
