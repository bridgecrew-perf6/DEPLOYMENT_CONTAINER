FROM python:3.6.9
COPY requirements.txt .
COPY . /apps
WORKDIR /apps
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /apps/
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 main:app