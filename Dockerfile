FROM ferumflex/conty
MAINTAINER Anton Pomieschenko<ferumflex@gmail.com>

# for speed up things. docker do not install it every time. only if requirements were changed
ADD www/requirements.txt /opt/django
RUN pip3.6 install -r /opt/django/requirements.txt

ADD www/requirements_test.txt /opt/django
RUN pip3.6 install -r /opt/django/requirements_test.txt

ADD www /opt/django/app
RUN python3.6 /opt/django/app/manage.py collectstatic --noinput

VOLUME ["/opt/django/persistent/media"]
EXPOSE 80

CMD python3.6 /opt/django/app/manage.py migrate --noinput && sh /opt/django/run.sh