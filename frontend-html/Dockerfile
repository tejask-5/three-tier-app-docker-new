FROM python:3
RUN apt-get update
RUN apt-get install openssh-server sudo net-tools -y
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 fwb
RUN echo 'fwb:fwb1234' | chpasswd
RUN service ssh start
RUN mkdir /home/ubuntu/code
WORKDIR /home/ubuntu/code
RUN chown fwb -R /home/ubuntu/code
ADD requirements.txt /home/ubuntu/code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 5001 22
CMD service ssh start && python3 front.py