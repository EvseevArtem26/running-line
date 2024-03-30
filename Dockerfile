FROM ubuntu:22.04

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

COPY . /app/

RUN apt-get update && \
  apt-get install imagemagick libmagick++-dev python3 python3-pip python3.10-venv -y

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install -r requirements.txt

COPY policy.xml /etc/ImageMagick-6/policy.xml

EXPOSE 9000

CMD [ "./startup.sh" ]