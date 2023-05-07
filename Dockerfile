FROM python:3.9.16-alpine3.16
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python application.py