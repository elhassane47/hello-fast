FROM python:3.8

WORKDIR /usr/src/app


COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt


COPY . /usr/src/app/


EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--reload", "main:app"]

