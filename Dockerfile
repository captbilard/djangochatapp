FROM python:3.8

# SET ENVIRONMENT VARIABLES
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#SET workdirectory
WORKDIR /code

#Install Dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

#COPY PROJECT
COPY . /code/

