FROM ubuntu:18.04
RUN apt-get update \
  && apt-get install -y python3.8 python3-pip python3.8-dev libpq-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && python3.8 -m pip install --upgrade pip \
  && apt-get install -y git
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN ls
RUN python3.8 -m pip install -r requirements.txt
EXPOSE 5000
CMD ["python3.8","app.py"]
