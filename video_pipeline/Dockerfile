FROM python:3.10.12-alpine3.18

WORKDIR /app

RUN apk add 

# RUN apt-get update && apt-get install --no-install-recommends -y \
#     ffmpeg \
#     && rm -rf /var/lib/apt/lists/*

RUN apk add --no-cache ffmpeg

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY converter.py .

RUN mkdir -p /videos

CMD ["python", "converter.py", "/videos"]