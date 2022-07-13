FROM python:3

WORKDIR app/

COPY . .

RUN apt update

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential

RUN python3 -m pip install -r requirements.txt

RUN python -m pip install mysqlclient