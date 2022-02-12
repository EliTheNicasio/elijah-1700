FROM ubuntu:18.04

RUN apt update -y
RUN apt-get -y install wget

# Download and install h2o wave
RUN wget https://github.com/h2oai/wave/releases/download/v0.16.0/wave-0.16.0-linux-amd64.tar.gz
RUN tar -xvf wave-0.16.0-linux-amd64.tar.gz && mv wave-0.16.0-linux-amd64 /wave && chmod +x /wave/waved
WORKDIR /wave
EXPOSE 10101/tcp

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8 

RUN apt-get -y install python3-pip
COPY . .
RUN pip3 install -r requirements.txt
RUN chmod +x UI_wrapper_script.sh

CMD ["./UI_wrapper_script.sh"]
