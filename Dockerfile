FROM python
RUN apt-get update
RUN apt-get upgrade -y
RUN cat /etc/os-release
RUN python -V
RUN mkdir -p /sample-demo
COPY ./src/ /sample-demo/src
COPY ./requirements.txt /sample-demo/
RUN pip install -r /sample-demo/requirements.txt
RUN python /sample-demo/src/package_test.py