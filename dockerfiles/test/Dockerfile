FROM		python:2.7
MAINTAINER	Alex Gao
WORKDIR		/code
COPY		./sources.list /etc/apt/
COPY		.ssh /root/.ssh/
RUN		chmod 400 /root/.ssh/id_rsa
RUN		apt-get update && apt-get install -y --force-yes xvfb
COPY    ./firefox-39.0.tar.bz2 /usr/lib/
RUN     pushd /usr/lib
RUN     tar -jxf /usr/lib/firefox-39.0.tar.bz2
RUN     popd
RUN     ln -s /usr/lib/firefox/firefox /usr/bin/
RUN		pip install --upgrade pip
