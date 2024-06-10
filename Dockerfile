FROM python:3.10.6-buster

COPY requirements_docker.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY consumption_prediction/api /
#COPY setup.py setup.py
#RUN pip install .

CMD uvicorn fast:app --host 0.0.0.0 --port $PORT
