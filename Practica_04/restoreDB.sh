#!/bin/bash

sudo docker-compose exec mongo /bin/bash

# En el Prompt nuevo
# mongorestore --drop dump