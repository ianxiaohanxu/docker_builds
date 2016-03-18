FROM		python:2.7
MAINTAINER	Alex Gao
WORKDIR		/code
COPY		./sources.list /etc/apt/
COPY		.ssh /root/.ssh/
RUN		chmod 400 /root/.ssh/id_rsa
RUN		apt-get update && apt-get install -y --force-yes xvfb firefox
RUN     apt-get remove -y --force-yes firefox
COPY    ./firefox /usr/lib/firefox/
RUN     ln -s /usr/lib/firefox/firefox /usr/bin/
RUN		pip install --upgrade pip
