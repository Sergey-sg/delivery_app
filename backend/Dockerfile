FROM python:3.8.10

WORKDIR /delivery_app_project

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

CMD python3 manage.py runserver 0.0.0.0:8000