# Use an official Apache Airflow runtime as a parent image
FROM apache/airflow:2.7.3-python3.11

USER root

# Installing postgresql
RUN apt-get update && \
    apt-get install -y gcc libpq-dev 

USER airflow

# Install Virtual Environment and Jupyterlab
RUN pip install --upgrade pip && \
    pip install apache-airflow[virtualenv]==2.7.3 &&\
    pip install jupyterlab==4.0.8 &&\
    pip install matplotlib==3.7.2




