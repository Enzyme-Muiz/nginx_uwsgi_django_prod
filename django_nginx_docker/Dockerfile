FROM python:3.8-slim-buster
RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc libc-dev python3-dev
RUN python -m venv env 
RUN . env/bin/activate
RUN pip install -r /requirements.txt
#RUN venv/Scripts/activate.bat
COPY ./ ./
#CMD [ "python", "./django_docker_nginx/manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["uwsgi", "--chdir", "/django_docker_nginx", "--socket", "0.0.0.0:8000", "--master", "--enable-threads", "--module", "django_docker_nginx.wsgi"]
#CMD ["uwsgi", "--chdir", "/django_docker_nginx", "--http", "0.0.0.0:8000", "--master", "--enable-threads", "--module", "django_docker_nginx.wsgi"]
CMD ["uwsgi", "--ini", "wsgii.ini"]