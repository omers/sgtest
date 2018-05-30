FROM python:3.6.5-alpine

RUN apk update && apk add py-configobj libusb py-pip python-dev gcc linux-headers musl-dev \
	libffi-dev openssl-dev
RUN mkdir /PythonApp/

ADD requirements.txt /PythonApp/
RUN pip install -r /PythonApp/requirements.txt

ADD . /PythonApp/

WORKDIR /PythonApp/
CMD python app.py
