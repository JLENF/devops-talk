FROM alpine:3.20

COPY . /app
WORKDIR /app

RUN apk add python3~=3.12 py3-pip~=24.0 --no-cache && python3 -m venv /appenv
RUN /appenv/bin/pip install -r /app/requirements.txt

EXPOSE 5000

CMD ["/appenv/bin/python", "/app/app.py"]
