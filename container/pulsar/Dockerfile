FROM apachepulsar/pulsar-all:3.1.0

# Add the NAR file and set permissions
# ADD https://github.com/streamnative/pulsar-io-lakehouse/releases/download/v3.1.0.3/pulsar-io-lakehouse-3.1.0.3.nar /pulsar/connectors/pulsar-io-lakehouse-3.1.0.3.nar

# Download the NAR file
ADD https://github.com/streamnative/pulsar-io-lakehouse/releases/download/v3.1.0.3/pulsar-io-lakehouse-3.1.0.3.nar /tmp/pulsar-io-lakehouse-3.1.0.3.nar

# Copy the file with permissions
COPY --chown=root:root /tmp/pulsar-io-lakehouse-3.1.0.3.nar /pulsar/connectors/pulsar-io-lakehouse-3.1.0.3.nar

# Copy the iceberg configuration file
COPY ./iceberg.json /pulsar/connectors/iceberg.json
