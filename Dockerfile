FROM python
RUN pip install flask
COPY app.py /opt/app.py
WORKDIR /opt
ENTRYPOINT [ "python", "app.py" ]
