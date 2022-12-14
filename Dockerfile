FROM python:3.9.12-slim-buster
#
RUN apt-get update
RUN apt-get install -y libmagic1 ffmpeg
RUN apt-get install -y pandoc
#
WORKDIR /AudioBridge/bin
COPY . /AudioBridge/bin
#
RUN pip install -r requirements.txt
#
ENTRYPOINT ["python3", "-Bu", "-m", "audiobridge"]
