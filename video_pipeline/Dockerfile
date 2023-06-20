FROM python:3.10-buster

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY converter.py .

RUN mkdir -p /videos

CMD [ "python", "converter.py" "/videos" ]