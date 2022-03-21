FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY ./checking.html /usr/share/nginx/html/index.html
COPY ./checking.html /usr/share/nginx/html/index2.html
COPY ./checking.html /home/www/index.html
COPY ./another.html /home/www/index2.html