FROM python:3-slim-buster

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 80/tcp
EXPOSE 80/udp

CMD ["streamlit", "run","./main.py",  "--server.port=8501", "--server.address=0.0.0.0"]