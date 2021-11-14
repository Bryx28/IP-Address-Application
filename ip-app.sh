#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp ipapp.py tempdir/.
cp ip_add_json.py  tempdir/.
cp ip_add_json2.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile

echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >>  tempdir/Dockerfile
echo "COPY  ipapp.py  /home/myapp/" >>  tempdir/Dockerfile
echo "COPY  ip_add_json.py  /home/myapp/" >>  tempdir/Dockerfile
echo "COPY  ip_add_json2.py  /home/myapp/" >>  tempdir/Dockerfile

echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/ipapp.py" >> tempdir/Dockerfile

cd tempdir
docker build -t ip_app .
docker run -t -d -p 8080:8080 --name ip_apprunning ip_app
docker ps -a