# LAB - Class 34
# Project: cookies-stands
# Author: Zekra Quraan


Setup
.env file content
~~~
SECRET_KEY=YU_AH2FvQjqG4b5V5yim4uIDOHoXjdc3HldkRhQJMBw
DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
ALLOW_ALL_ORIGINS=True
# postgres://nzfhrkcw:vhS5Nml1pXe75YCFGMH6eRXD1kgno8ms@peanut.db.elephantsql.com/nzfhrkcw
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=nzfhrkcw
DATABASE_USER=nzfhrkcw
DATABASE_PASSWORD=vhS5Nml1pXe75YCFGMH6eRXD1kgno8ms
DATABASE_HOST=peanut.db.elephantsql.com
DATABASE_PORT=5432
~~~

PORT - 8000
DATABASE_URL - postgres://nzfhrkcw:vhS5Nml1pXe75YCFGMH6eRXD1kgno8ms@peanut.db.elephantsql.com/nzfhrkcw

How to initialize/run your application (where applicable)
docker-compose run web python manage.py runserver

