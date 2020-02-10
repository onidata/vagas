FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /onidataProject
WORKDIR /onidataProject
ADD requirements.txt /onidataProject/
RUN pip install -r requirements.txt
ADD . ../onidataProject/
