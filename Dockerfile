FROM alpine:3.20

COPY . /app
WORKDIR /app

RUN apk update && apk add python3~=3.12 py3-pip~=3.12 && python3 -m venv /appenv
RUN /appenv/bin/pip install -r /app/requirements.txt

EXPOSE 5000
CMD ["/appenv/bin/python", "/app/app.py"]
