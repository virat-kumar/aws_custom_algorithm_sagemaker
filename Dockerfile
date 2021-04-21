FROM ubuntu

RUN apt-get -y update && apt-get install -y wget python3 nginx ca-certificates 

RUN apt install -y nginx python3-pip gunicorn

RUN pip3 install catboost flask 

RUN pip3 install  gevent
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY Linear_Regx /opt/program

RUN chmod +x /opt/program/serve
WORKDIR /opt/program

# RUN /opt/program/serve