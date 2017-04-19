FROM python:3
ADD build /build
WORKDIR /build
RUN apt-get update && \
    apt-get install -y dos2unix
RUN dos2unix bower_install.sh
RUN pip install -r requirements.txt
RUN chmod +x bower_install.sh
RUN ./bower_install.sh
ADD code /code
WORKDIR /code
RUN bower install
CMD [ "python", "serve.py" ]