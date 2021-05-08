FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD python app/main.py