
FROM ubuntu

MAINTAINER Nick Kopyt

RUN apt-get update; apt-get install -y python3 python3-pip

RUN pip install flask==2.1.2

WORKDIR /flask_application

COPY . .

ENTRYPOINT ["python3", "dz7.py" ]


