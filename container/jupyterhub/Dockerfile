# Start from the base jupyter notebook image
FROM jupyter/base-notebook:latest

# Switch to the root user so we can install additional packages.
USER root

# Install some additional OS packages for use with some Python libraries.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libatlas-base-dev gfortran gcc python3-dev libpq-dev openssh-client cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y build-essential 

RUN apt-get install -y libssl-dev 

RUN apt-get install -y libffi-dev 

RUN apt-get install git-all


# Grant jovyan password-less sudo for specific cron commands
RUN echo "$NB_USER ALL=(ALL) NOPASSWD: /usr/sbin/service cron start" >> /etc/sudoers.d/jovyan && \
    echo "$NB_USER ALL=(ALL) NOPASSWD: /usr/sbin/service cron stop" >> /etc/sudoers.d/jovyan && \
    echo "$NB_USER ALL=(ALL) NOPASSWD: /usr/sbin/service cron restart" >> /etc/sudoers.d/jovyan && \
    chmod 0440 /etc/sudoers.d/jovyan


# Switch back to jovyan (default user) and install Python packages.
USER $NB_UID

# Copy requirements.txt and install required Python packages.
COPY ./requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

RUN git clone https://github.com/apache/iceberg.git
RUN cd iceberg/python
RUN pip install -e .

RUN git clone https://github.com/minio/minio-py
RUN cd minio-py
RUN python setup.py install

# Copy the assets folder
COPY ./assets /home/jovyan/assets
USER root
RUN chmod -R 700 /home/jovyan/assets

USER $NB_UID

# We will start the notebook with the base-notebook start script.
CMD ["start.sh", "jupyter", "lab"]
