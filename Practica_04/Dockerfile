# flask_dockerfile

FROM python:3.7

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development
ENV FLASK_DEBUG 1

RUN apt-get install libjpeg-dev \
                       zlib1g-dev \
                       libfreetype6-dev \
                       liblcms2-dev 
RUN pip install --upgrade pip
                      
                       
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["flask", "run"]
