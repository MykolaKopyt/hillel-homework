
FROM ubuntu

MAINTAINER Nick Kopyt

RUN apt-get update; apt-get install -y python3 python3-pip

RUN pip install flask==2.1.2

WORKDIR /flask_docker

COPY . .

ENTRYPOINT ["python3"]

CMD ["dz7.py"]

