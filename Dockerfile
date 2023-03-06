FROM python:3.8-alpine

COPY bot/Main.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "Main.py"]