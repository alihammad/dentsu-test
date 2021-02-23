#!/bin/sh

rm -f data/*
python3 app/json2csv.py 
docker-compose down
docker system prune -a -f
docker-compose up --build
