FROM python:3.10.8-bullseye

WORKDIR /flask-be-api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "--app", "main.py", "run", "--host=0.0.0.0"]