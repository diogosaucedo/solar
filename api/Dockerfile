FROM python:3.12-slim

WORKDIR /app/api

COPY ./ ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]