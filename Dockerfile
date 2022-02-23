FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
COPY docker_entrypoint.sh docker_entrypoint.sh
RUN pip3 install -r requirements.txt

RUN apt-get update
RUN apt-get install curl -y
RUN curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash
RUN apt-get install speedtest

COPY . .

ENTRYPOINT ["/bin/bash"]
CMD ["docker_entrypoint.sh"]