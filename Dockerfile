FROM python:3

WORKDIR / project

COPY . .

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD ["main.py"]

ENTRYPOINT ["python3"]