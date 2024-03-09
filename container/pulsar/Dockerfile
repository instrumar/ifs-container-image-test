# Use the Pulsar image
FROM apachepulsar/pulsar-all:3.2.1

# Switch to root user to install packages
USER root

# Install required packages for building Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    liblzma-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev

# Download Python 3.11 and extract it
RUN curl -O https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tar.xz \
    && tar -xf Python-3.11.0.tar.xz

# Configure & install Python 3.11
RUN cd Python-3.11.0 \
    && ./configure --enable-optimizations \
    && make -j $(nproc) \
    && make altinstall

# Install pip for Python 3.11
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# Install Python packages using the newly installed Python 3.11
RUN python3.11 -m pip install requests

# Continue with the rest of your Dockerfile...
# ADD https://github.com/streamnative/kop/releases/download/v3.1.1.1/pulsar-protocol-handler-kafka-3.1.1.1.nar /tmp/pulsar-protocol-handler-kafka-3.1.1.1.nar
# COPY --from=downloader /tmp/pulsar-protocol-handler-kafka-3.1.1.1.nar /protocols/pulsar-protocol-handler-kafka-3.1.1.1.nar
# COPY ./iceberg.json /pulsar/connectors/iceberg.json

