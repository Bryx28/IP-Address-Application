FROM python
RUN pip install flask
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY  ipapp.py  /home/myapp/
COPY  ip_add_json.py  /home/myapp/
COPY  ip_add_json2.py  /home/myapp/
EXPOSE 8080
CMD python /home/myapp/ipapp.py
