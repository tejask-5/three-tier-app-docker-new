FROM python:3
RUN apt-get update
RUN apt-get install openssh-server sudo net-tools -y
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G root -u 1000 fwb
RUN service ssh start
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
RUN chmod -R 775 /code/
EXPOSE 5001 22
CMD service ssh start && python3 front.py
