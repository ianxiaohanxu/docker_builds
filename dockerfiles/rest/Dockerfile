FROM        python:2.7
MAINTAINER  Alex Gao (alex@gatherhealth.com)
EXPOSE      8081
WORKDIR     /code
COPY        sources.list /etc/apt/
COPY        .ssh /root/.ssh/
RUN	    chmod 400 /root/.ssh/id_rsa
COPY        dev_reset /root/python_modules/dev_reset/
RUN         apt-get update && apt-get install -y --force-yes postgresql-client expect libyaml-dev
RUN         pip install --upgrade pip
ENV         PYTHON_PIP_VERSION 8.0.2
RUN         pip install phonenumbers==7.2.3
RUN         pip install simplejson==3.6.4
CMD         ["bash"]
