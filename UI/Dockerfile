FROM ubuntu:18.04
RUN apt update -y
RUN apt-get -y install wget
RUN wget https://github.com/h2oai/wave/releases/download/v0.16.0/wave-0.16.0-linux-amd64.tar.gz
RUN tar -xvf wave-0.16.0-linux-amd64.tar.gz && mv wave-0.16.0-linux-amd64 /wave && chmod +x /wave/waved
EXPOSE 10101/tcp
RUN apt-get -y install python3-pip
COPY . /usr/src/app
RUN pip3 install -r /usr/src/app/requirements.txt
RUN chmod +x /usr/src/app/UI_wrapper_script.sh
CMD ["./usr/src/app/UI_wrapper_script.sh"]
