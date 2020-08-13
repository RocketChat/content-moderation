FROM python:3

MAINTAINER shreyansh-tomar

RUN pip install --upgrade pip

RUN pip install torch torchvision

RUN pip install -U Flask
RUN pip install requests
RUN pip install gunicorn

WORKDIR /app
COPY . /app

EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-b", ":5000", "-t", "360", "--reload", "wsgi:app"]

