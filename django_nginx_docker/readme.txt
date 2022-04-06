run the two codes below from the current directory
docker build -t wsgi .
docker run -p 8080:8000 wsgi
open it at http://localhost:8000/



##
to run the dockerfile with cmd "uwsgi --ini wsgii.ini" ensure the wsgi.py has os.environ['DJANGO_SETTINGS_MODULE'] = 'django_docker_nginx.settings.dev'
not 
this 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_docker_nginx.settings.dev') 



#to start the docker-compose
go to the directory where the yml file is and type docker-compose up --build



# I pushed the nginx_part to docker up
by: docker build -t rajimu/nginx_part .
then: docker push rajimu/nginx_part