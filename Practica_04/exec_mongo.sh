#!/bin/bash

sudo docker-compose exec mongo /bin/bash
sudo mongorestore --drop dump
