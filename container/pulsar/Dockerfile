# Use the Pulsar image
FROM apachepulsar/pulsar-all:3.1.1

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
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

# Download Python 3.11, extract, configure, make, and install
RUN curl -O https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tar.xz \
    && tar -xf Python-3.11.0.tar.xz \
    && cd Python-3.11.0 \
    && ./configure --enable-optimizations \
    && make -j $(nproc) \
    && make altinstall

# Update the symbolic links for Python3 and Pip3 to point to Python 3.11
RUN update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.11 1 \
    && update-alternatives --set python3 /usr/local/bin/python3.11 \
    && update-alternatives --set pip3 /usr/local/bin/pip3.11

# Install pip for Python 3.11
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# Install Python packages using the newly installed Python 3.11
RUN python3.11 -m pip install requests

# Continue with the rest of your Dockerfile...
# ADD https://github.com/streamnative/kop/releases/download/v3.1.1.1/pulsar-protocol-handler-kafka-3.1.1.1.nar /tmp/pulsar-protocol-handler-kafka-3.1.1.1.nar
# COPY --from=downloader /tmp/pulsar-protocol-handler-kafka-3.1.1.1.nar /protocols/pulsar-protocol-handler-kafka-3.1.1.1.nar
# COPY ./iceberg.json /pulsar/connectors/iceberg.json
