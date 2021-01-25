FROM python:3.8

RUN mkdir /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]
