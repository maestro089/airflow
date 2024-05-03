FROM python:3.11
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT celery -app worker worker --loglevel=INFO