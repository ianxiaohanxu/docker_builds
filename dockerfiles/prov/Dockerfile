FROM        python:2.7
MAINTAINER  Alex Gao (alex@gatherhealth.com)
COPY        sources.list /etc/apt/
COPY        .ssh /root/.ssh/
RUN         chmod 400 /root/.ssh/id_rsa
RUN         apt-get update && apt-get install -y --force-yes postgresql-client gettext
RUN         pip install --upgrade pip
ENV         PYTHON_PIP_VERSION 8.0.2
EXPOSE      8000
WORKDIR     /code
CMD         ["bash"]
