FROM python:3.8-slim-bullseye

COPY /bot/ /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python", "Main.py"]